# Final Version
import os
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk


def load_master_dicts():
    positive_words = set()
    negative_words = set()
    
    with open('MasterDictionary/positive-words.txt', 'r') as f:
        positive_words.update(f.read().splitlines())
    
    with open('MasterDictionary/negative-words.txt', 'r') as f:
        negative_words.update(f.read().splitlines())
        
    return positive_words, negative_words


def load_stopwords_from_folder(folder):
    stop_words = set()
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            with open(filepath, 'r') as f:
                stop_words.update(f.read().splitlines())
    return list(stop_words)


def preprocess_text(text, custom_stop_words):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    stop_words = set(custom_stop_words)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    return tokens


def compute_sentiment_scores(tokens, positive_words, negative_words):
    positive_score = sum(1 for word in tokens if word in positive_words)
    negative_score = sum(1 for word in tokens if word in negative_words)
    
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(tokens) + 0.000001)
    
    return positive_score, negative_score, polarity_score, subjectivity_score


def compute_readability_metrics(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    avg_sentence_length = len(words) / len(sentences)
    
    complex_words = [word for word in words if len([syll for syll in re.findall(r'[aeiouyAEIOUY]', word)]) > 2]
    percentage_complex_words = len(complex_words) / len(words)
    
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    return avg_sentence_length, percentage_complex_words, fog_index

def compute_other_metrics(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    avg_words_per_sentence = len(words) / len(sentences)
    
    complex_words = [word for word in words if len([syll for syll in re.findall(r'[aeiouyAEIOUY]', word)]) > 2]
    complex_word_count = len(complex_words)
    
    word_count = len(words)
    
    syllables_per_word = sum(len(re.findall(r'[aeiouyAEIOUY]', word)) for word in words) / len(words)
    
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    return avg_words_per_sentence, complex_word_count, word_count, syllables_per_word, personal_pronouns, avg_word_length


def extract_article_data(url, file_id, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs(response.content, 'html.parser')
        desired_classes = ['td-post-content tagdiv-type', 'tdb-block-inner td-fix-index']
        title_element = soup.find('title')
        text_elements = soup.find_all('div', class_=desired_classes)
        
        if title_element and text_elements:
            title = title_element.text.strip()
            text = '\n'.join([p.text.strip() for p in text_elements])
            filename = os.path.join(folder, f"{file_id}.txt")
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Title: {title}\n\n")
                f.write(text)
            
            return {'title': title, 'text': text}
    except requests.exceptions.RequestException as e:
        print(f"Website Not Found {url}: {e}")
        return None

def main():
    positive_words, negative_words = load_master_dicts()
    custom_stopwords_folder = 'StopWords'
    custom_stop_words = load_stopwords_from_folder(custom_stopwords_folder)

    articles_folder = 'articles'
    if not os.path.exists(articles_folder):
        os.makedirs(articles_folder)
    
    
    df = pd.read_excel('Input.xlsx')
    urls = df['URL'].tolist()  
    
    analysis_results = []
    

    for i, url in enumerate(urls):
        file_id = f"blackassign{i+1:04d}"  
        article_data = extract_article_data(url, file_id, articles_folder)
        
        if article_data:
            title = article_data['title']
            text = article_data['text']
            tokens = preprocess_text(text, custom_stop_words)
            positive_score, negative_score, polarity_score, subjectivity_score = compute_sentiment_scores(tokens, positive_words, negative_words)
            avg_sentence_length, percentage_complex_words, fog_index = compute_readability_metrics(text)
            avg_words_per_sentence, complex_word_count, word_count, syllables_per_word, personal_pronouns, avg_word_length = compute_other_metrics(text)
            analysis_results.append({
                'URL': url,
                'POSITIVE SCORE': positive_score,
                'NEGATIVE SCORE': negative_score,
                'POLARITY SCORE': polarity_score,
                'SUBJECTIVITY SCORE': subjectivity_score,
                'AVG SENTENCE LENGTH': avg_sentence_length,
                'PERCENTAGE OF COMPLEX WORDS': percentage_complex_words,
                'FOG INDEX': fog_index,
                'AVG NUMBER OF WORDS PER SENTENCE': avg_words_per_sentence,
                'COMPLEX WORD COUNT': complex_word_count,
                'WORD COUNT': word_count,
                'SYLLABLE PER WORD': syllables_per_word,
                'PERSONAL PRONOUNS': personal_pronouns,
                'AVG WORD LENGTH': avg_word_length
            })
    
    results_df = pd.DataFrame(analysis_results)
    output_df = pd.merge(df, results_df, on='URL')
    output_df.to_excel('Output Data Structure.xlsx', index=False)

if __name__ == "__main__":
    main()


# Project Title & Description

Data-Extraction-and-NLP 

 Black-Coffer assignment link : https://drive.google.com/drive/u/0/mobile/folders/1ltdsXAS_zaZ3hI-q9eze_QCzHciyYAJY?usp=sharing 


## Screenshots

Input excel file with urls
![Alt Text](https://github.com/Aravindraprasad/Data-Extraction-and-NLP-Black-Coffer/blob/main/Project%20Images/input_xlsx_file.jpg?raw=True)

Output exceel file with Analysis

![Alt Text](https://github.com/Aravindraprasad/Data-Extraction-and-NLP-Black-Coffer/blob/main/Project%20Images/output_xlsx_file.jpg?raw=True)


# Explaining approached  solution:

Step 1 :
Environment Setup
Install necessary Python packages: nltk, requests, pandas, beautifulsoup4, and openpyxl

Step 2 :
Text Extraction:
For each URL in Input.xlsx fetch the HTML content parse it to extract the article's text and save it to a text file in the articles folder

Step 3 :
Text Preprocessing:
Convert the text to lowercase remove punctuation and filter out stop words 

Step 4 :
Sentiment Analysis:
Calculate Positive Score by counting the number of positive words
Calculate Negative Score by counting the number of negative words
Compute Polarity Score and Subjectivity Score using provided formulas

Step 5 :
Results:
Computed data with the input data and save the results to Output Data Structure.xlsx











## Installation

Install my-project 

```bash
pip install -r requirements.txt
```

B. How to run the .py file to generate output


Step 2:
```bash
If Folder is in Zip formate then Unzip it

```


Step 3:
Run the python file
```bash
run main.py
```
Step 4
Include all dependencies required
```bash
Dependencies are in requirements.txt file
```

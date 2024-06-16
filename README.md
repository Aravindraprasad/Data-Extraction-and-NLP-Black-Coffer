
# Project Title & Description

Data-Extraction-and-NLP : Black-Coffer 


## Screenshots

# Input Excel file with URLs
![Alt Text](https://github.com/Aravindraprasad/Data-Extraction-and-NLP-Black-Coffer/blob/main/Project%20Images/input_xlsx_file.jpg?raw=True)

# Output Excel file with Analysis


![Alt Text](https://github.com/Aravindraprasad/Data-Extraction-and-NLP-Black-Coffer/blob/main/Project%20Images/output_xlsx_file.jpg?raw=True)

# Data Extraction

Input: "input.xlsx" file containing article URLs with IDs.
Output: Text files named after URL_IDs containing extracted article text (title and body).
Libraries: BeautifulSoup, Selenium, Scrapy (choose one).

# Extraction Logic
Download article content using the chosen library.
Parse HTML with BeautifulSoup.
Identify and extract elements containing title and body text (avoid headers and footers).
Save extracted text to a file named after URL_ID.

# Data Analysis

Input: Extracted text files.
Output: Excel file ("Output Data Structure.xlsx") with computed variables for each article.
Text Analysis (Details not provided, can be implemented based on specific requirements):
Example: Word frequency, sentiment analysis, readability score.
Save results in the specified format ("Output Data Structure.xlsx").





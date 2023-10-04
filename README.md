# Web Scraping and Chatbot Assignment
This project demonstrates web scraping of a provided website and generating responses using OpenAI's GPT-3.5 language model.

### Table of Contents
* Introduction
* Web Scraping
* Chatbot
* Usage
* Requirements
* Setup
* Example Usage

### Introduction
This project combines web scraping and natural language processing to extract information from a given website and generate conversational responses using GPT-3.5 from OpenAI.

### Web Scraping
The web_scraping.py script uses Python and the BeautifulSoup library to scrape headers, paragraphs, and links from a provided website.

### test.py
The chatbot uses GPT-3.5 from OpenAI to generate responses based on user input and the scraped website data. The chatbot.py script sets up the chatbot interaction using the OpenAI API.

### Usage
1. Set up the OpenAI API and obtain an API key.
2. Run the test.py script, interact with the chatbot by providing input, and receive conversational responses.
   
### Requirements
* Python 3.x
* Requests
* BeautifulSoup
* OpenAI API key

### Setup
Install the required libraries using pip:
```
  pip install requests beautifulsoup4 openai
```
Set up an OpenAI account and obtain an API key.
Update the openai.api_key variable in the test.py script with your API key.

### Example Usage
Run the test.py script to initiate a conversation with the chatbot.

  python test.py
### 1> Adding a Wikipedia URL
<img width="752" alt="img1" src="https://github.com/sejalsharma0138/OpenAI-Assignment/assets/66528532/f89dcfc0-6569-416e-8aa5-627b54ea66ce">

### 2> Adding an inaccessible URL
<img width="744" alt="img2" src="https://github.com/sejalsharma0138/OpenAI-Assignment/assets/66528532/d313c0ea-5d38-49d1-9765-caa266bd1070">

### 3> Adding Resume data
<img width="750" alt="img3" src="https://github.com/sejalsharma0138/OpenAI-Assignment/assets/66528532/754df94d-922d-450b-9847-fb146e483c1b">





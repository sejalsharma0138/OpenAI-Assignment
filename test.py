
## PART-1 Web Scraping 


import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    # Send a request to the URL and retrieve the page content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch content from the URL.")
        return None
    return response.content

def extract_information(content, output_file):
    soup = BeautifulSoup(content, 'html.parser')

    # Initialize a list to store extracted information
    extracted_data = []

    # Extract headers (h1 to h6) and paragraphs
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    paragraphs = soup.find_all('p')
    links = soup.find_all('a')

    # Add headers and paragraphs to the extracted data
    for header in headers:
        extracted_data.append(header.text.strip())

    for paragraph in paragraphs:
        extracted_data.append(paragraph.text.strip())

   # for link in links:
    #    extracted_data.append(link['href'])

## PART-2 Extracting the scraped information in a text document

    # Write the extracted information to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for item in extracted_data:
            file.write(item + '\n')

    print(f"Extracted information saved to {output_file}")



if __name__ == "__main__":
    # Provide the URL of the website you want to scrape
    url = input("Enter the website url")

    # Fetch website content
    content = fetch_website_content(url)

    if content:
        # Define the output file for the database
        output_file = "database.txt"

        # Extract relevant information and save to the database
        extract_information(content, output_file)
    else:
        print("No content fetched.")



def read_sent_files(file_paths):
    data = ""
    for file_path in file_paths:
        with open(file_path, "r",encoding="utf8") as file:
            data += file.read() + "\n"  # Separate data from different files
    return data

# Example usage
file_paths = ["database.txt"]
sent_data = read_sent_files(file_paths)

import openai

# Set up OpenAI API client
openai.api_key = "Your Key"

def generate_response(user_input, sent_data):
    prompt = f"User: {user_input}\nSent Data: {sent_data}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Example usage

print("Bot: What do you want to know?  type exit to quit." )

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = generate_response(user_input, sent_data)
    print("Bot:", response)



   
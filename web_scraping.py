import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    # Sending a request to the URL and retrieve the page content
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch content from the URL.")
        return None
    return response.content

def extract_information(content, output_file):
    soup = BeautifulSoup(content, 'html.parser')

    # Initializing a list to store extracted information
    extracted_data = []

    # Extracting headers (h1 to h6) and paragraphs
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

    # Writing the extracted information to the output file
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
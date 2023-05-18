import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
import re

def get_unique_words(url):
    # Fetch the HTML content of the website
    response = requests.get(url)
    html_content = response.text
    
    # Extract text from HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    # Split the text into words
    words = cleaned_text.split()
    # Count the frequency of each word
    word_count = Counter(words)
    # Convert the result to JSON format
    json_result = json.dumps(word_count, indent=4)
    return json_result
# function terminated
# Example usage
website_url = input("Enter the URL of a static website: ")
result = get_unique_words(website_url)
print(result)

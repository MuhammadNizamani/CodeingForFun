import requests
from bs4 import BeautifulSoup

def search_product(url, product_name):
    # Send GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup)
    # Find all the anime titles on the page
    anime_titles = soup.find_all('a')
    
    # Search for the given product name in the list of anime titles
    for i, anime_title in enumerate(anime_titles):
        if anime_title.text.strip() == product_name:
            return i + 1
    
    # If the product was not found, return None
    return None

# Test the function with the given URL and product name
url = "https://www3.gogoanimes.fi/anime-list-A"
product_name = "A Day Before Us"
product_index = search_product(url, product_name)

if product_index:
    print(f"The product '{product_name}' was found at index {product_index}.")
else:
    print(f"The product '{product_name}' was not found on the website.")

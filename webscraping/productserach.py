import requests
from bs4 import BeautifulSoup

def search_product(url, product_name):
    # Send GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup)
    # Find all the anime titles on the page
    anime_titles = soup.find_all('a',)
    # print(anime_titles)
    # Search for the given product name in the list of anime titles
    for i, anime_title in enumerate(anime_titles):
        if anime_title.text.strip() == product_name:
             
            return str(anime_title)
    
    # If the product was not found, return None
    return None

# Test the function with the given URL and product name
url = "https://www3.gogoanimes.fi/anime-list-A"
product_name = "A Day Before Us"
html = search_product(url, product_name)

# if product_index:
#     print(f"The product '{product_name}' was found at index {product_index}.")
# else:
#     print(f"The product '{product_name}' was not found on the website.")

# print(type(anime_link))
print(html)

# Sample HTML code
# html = '<a href="/category/ai-no-wakakusa-monogatari" title="">Ai no Wakakusa Monogatari</a>'

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Get the `href` attribute value of the `a` tag
href = soup.a['href']

# Get the text content of the `a` tag
text = soup.a.text

# Print the `href` attribute value and text content
print(f"href: {href}")
print(f"text: {text}")
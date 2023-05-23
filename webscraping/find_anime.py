import requests
from bs4 import BeautifulSoup
class Anime:
    def __init__(self, url1= 'https://www3.gogoanimes.fi/'):
        self.url1 = url1
    def merge_link(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Get the `href` attribute value of the `a` tag
        href = soup.a['href']
        print(self.url1+href)
        return self.url1+href
    
    def search_product(self, url, product_name):
         

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

                
                return self.merge_link(str(anime_title))
    
        # If the product was not found, return None
        return None
    

    
anime = Anime()
url = "https://www3.gogoanimes.fi/anime-list-A"
product_name = "A Day Before Us"
html = anime.search_product(url, product_name)
print(html)
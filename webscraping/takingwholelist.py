import requests
from bs4 import BeautifulSoup
class Anime:
    def __init__(self, url1= 'https://www3.gogoanimes.fi/'):
        self.url1 = url1
    def merge_link(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Get the `href` attribute value of the `a` tag
        href = soup.a['href']
        # print(self.url1+href)
        return self.url1+href
    
    def search_anime(self, url= 'https://www3.gogoanimes.fi/anime-list-A'):
        animeList = []
        Isanimelist = False
        # Send GET request to the URL and get the HTML content
        response = requests.get(url)
        html_content = response.text
    
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        anime_titles = soup.find_all('a',)
        # Search for the given product name in the list of anime titles
        for i, anime_title in enumerate(anime_titles):
                if anime_title.text.strip() == "A Channel":
                     Isanimelist = True
                if Isanimelist:
                    # print(anime_title.text.strip())
                    animeList.append(self.merge_link(str(anime_title)))
                if anime_title.text.strip() == "Ai Tenchi Muyou!":
                    Isanimelist= False
                   
    
         
        return animeList
    

    
# anime = Anime()
# html = anime.search_anime()
# for link in html:
#      print(link)

    
import requests
from bs4 import BeautifulSoup
iswanted = False
url = "https://www3.gogoanimes.fi//category/addiction-to-wife-doting"
response = requests.get(url)
html_content = response.text
    
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup)
# Find all the anime titles on the page
anime_titles = soup.find_all('p',)

for i, anime_title in enumerate(anime_titles):
    if "Type:" in anime_title.text.strip() :
        iswanted = True
    if "Episode " in anime_title.text.strip():
        iswanted = False
    if iswanted:
        # print(anime_title)
        # my_string=str(anime_title.text.strip())
        # print("\n".join([line for line in my_string.split("\n") if line.strip()]))
        print(anime_title.text.strip())
        
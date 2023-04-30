import requests
from bs4 import BeautifulSoup

url = "https://www3.gogoanimes.fi//category/addiction-to-wife-doting"
response = requests.get(url)
html_content = response.text
    
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
#print(soup)
# Find all the anime titles on the page
anime_titles = soup.find_all('p',)
for i, anime_title in enumerate(anime_titles):
    print(str(anime_title.text.strip()))
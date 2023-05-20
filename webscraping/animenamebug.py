import requests
from bs4 import BeautifulSoup
response = requests.get('https://www3.gogoanimes.fi//category/ai-no-idenshi')
html_content = response.text
    
soup = BeautifulSoup(html_content, 'html.parser')
anime_name= soup.find_all('h1',)
full ="name:"+str(anime_name[0].text)
print(full) 

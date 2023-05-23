import requests
from bs4 import BeautifulSoup
import pandas as pd
from takingwholelist import Anime

def one_anime_data(url):
    isnameadded = True
    detaillist = []
    anime_data_dist = {}
    iswanted = False
    response = requests.get(url)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    anime_titles = soup.find_all('p',)
    anime_name= soup.find_all('h1',)
    full ="name:"+str(anime_name[0].text)

    for i, anime_title in enumerate(anime_titles):
        if isnameadded:
            detaillist.append(str(full))
            isnameadded = False

        if "Type:" in anime_title.text.strip() :
            iswanted = True
        if "Episode " in anime_title.text.strip():
            iswanted = False
        if iswanted:
            detaillist.append(str(anime_title.text.strip()))

    # print("\n\n outside the list")
    for idx in range(int(len(detaillist))):
        my_string = detaillist[idx] 
        my_string = my_string.replace('\n', '')
        split_string = my_string.split(':')
        anime_data_dist[split_string[0]] = split_string[1]
    return anime_data_dist
anime = Anime()
animelink = anime.search_anime()
list_of_dict_data = []
i = 1
for one_anime in animelink:
    print(f"Data is taking from link number {i}")
    list_of_dict_data.append(one_anime_data(one_anime))
    i+=1
    

df = pd.DataFrame(list_of_dict_data)
df.to_csv('data_37.csv', index=False)
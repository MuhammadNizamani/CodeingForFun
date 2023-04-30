import requests
from bs4 import BeautifulSoup
import pandas as pd
from takingwholelist import Anime

# detaillist = []
# anime_data_dist = {}
# iswanted = False
# url = "https://www3.gogoanimes.fi//category/ai-no-kusabi-2012-dub"
def one_anime_data(url):
    detaillist = []
    anime_data_dist = {}
    iswanted = False
    response = requests.get(url)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
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
            # print(anime_title.text.strip())
            detaillist.append(str(anime_title.text.strip()))

    # print("\n\n outside the list")
    for idx in range(int(len(detaillist))):
        my_string = detaillist[idx] 
        my_string = my_string.replace('\n', '')
        split_string = my_string.split(':')
        anime_data_dist[split_string[0]] = split_string[1]
    return anime_data_dist
# print(type(my_string))
i=0
anime = Anime()
animelink = anime.search_anime()
list_of_dict_data = []
# df = pd.DataFrame(columns=['Type', 'Plot Summary', 'Genre','Released', 'Status', 'Other name'])
for one_anime in animelink:
    
    list_of_dict_data.append(one_anime_data(one_anime))
     

df = pd.DataFrame(list_of_dict_data)
df.to_csv('data_A.csv', index=False)
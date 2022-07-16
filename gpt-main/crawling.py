import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://m.cafe.daum.net/kidchoir/5Hf2/7?listURI=%2Fkidchoir%2F5Hf2'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#mArticle > div.view_info')
    data=pd.DataFrame(title)
    data.to_csv('동요가사.csv', encoding='utf-8')
else : 
    print(response.status_code)
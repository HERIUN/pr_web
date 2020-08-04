

import requests
from bs4 import BeautifulSoup
import csv

# def get_news_soup_objects():
soup_objects = []

URL = 'https://movie.naver.com/movie/running/current.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select(
'div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul[class=lst_detail_t1] > li'
)

for movie in movie_section:
        
        a_tag = movie.select_one('dl > dt > a')

        movie_title = a_tag.get_text() # or a_tag.text
        movie_link = a_tag['href'].split('=')[1]

        data = {
            'title' : movie_title,
            'code' : movie_link
        }
        print(data)

        # with open('review.csv', 'a', encoding='utf-8-sig', newline="") as csvfile:
        #     fieldname = ['title', 'link']
        #     csvwriter = csv.DictWriter(csvfile, fieldname)
        #     csvwriter.writerow(data)
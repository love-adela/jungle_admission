import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbjungle

# 매트릭스와 같은 별점의 영화 찾기
target_movie = db.movie.find_one({'title':'매트릭스'})
target_star = target_movie['star']
movies = list(db.movie.find({'star':target_star}))
for movie in movies:
    print(movie['title'])

# 매트릭스 영화 별점 바꾸기
db.movie.update_one({'title': '매트릭스'}, {'$set': {'star': 0}})
target_movie = db.movie.find_one({'title':'매트릭스'})
target_star = target_movie['star']
print(target_star)
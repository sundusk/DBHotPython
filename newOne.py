import requests
from bs4 import BeautifulSoup

# 获取豆瓣评分前n的电影
def get_top_movies(n):
    if n > 250 or n < 1:
        print("输入的数字必须在1到250之间")
        return []
    
    url = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    top_movies = []
    items = soup.find_all('div', class_='item')
    for item in items[:n]:
        title = item.find('span', class_='title').text
        rating = item.find('span', class_='rating_num').text
        top_movies.append({'title': title, 'rating': rating})
    
    return top_movies

# 获取用户输入并打印前n的电影及其评分并保存到文本文件
while True:
    try:
        num_movies = int(input("请输入要获取的电影数量（1到250之间）："))
        if num_movies < 1 or num_movies > 250:
            print("输入的数字必须在1到250之间，请重新输入")
        else:
            break
    except ValueError:
        print("请输入一个有效的数字")

top_movies = get_top_movies(num_movies)
with open('top_movies.txt', 'w', encoding='utf-8') as f:
    for idx, movie in enumerate(top_movies, start=1):
        f.write(f"{idx}. {movie['title']} - {movie['rating']}\n")

for idx, movie in enumerate(top_movies, start=1):
    print(f"{idx}. {movie['title']} - {movie['rating']}")
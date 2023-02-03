import requests
from bs4 import BeautifulSoup

url ="http://www.cgv.co.kr/movies/?lt=1&ft=0"
window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=window_headers)
html = req.text
soup = BeautifulSoup(html, "html.parser")

movie_chart_all = soup.select_one('.sect-movie-chart')
movie_chart = movie_chart_all.select('li')

for rank,movie in enumerate(movie_chart,1):
    title=movie.select_one(".title")
    score = movie.select_one(".score")
    ticketing =score.select_one(".percent")
    egg_score = score.select_one(".egg-gage.small > .percent")
    open_date = movie.select_one(".txt-info > strong").next_element
    # next_element 처음 사용
    print(f"<<{rank}위>>")
    print(f"제목: {title.text}")
    # get_text활용법 처음 배움 
    print(ticketing.get_text(" : "))
    print(f"에그지수 = {egg_score.text}")
    print(f"{open_date.strip()} 개봉")
    print()

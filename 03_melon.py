import requests
from bs4 import BeautifulSoup

url ="https://www.melon.com/chart/index.htm"
window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=window_headers)
html = req.text
soup = BeautifulSoup(html,"html.parser")

list_50=soup.select(".lst50")
list_100=soup.select(".lst100")

list_all=list_50+list_100

for rank,i in enumerate(list_all,1):
    title= i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 > a")
    # 자식 태그 가리킬 때는 '>' 입력해주면 된다
    print(f"{rank}: {title.text}")
    print(singer.text)
    print()
import requests
from bs4 import BeautifulSoup

base_url ="https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword=input("검색어 입력하세요 : ")

url =base_url + keyword

window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

sample_naver= requests.get(url, headers=window_headers)

naver_html = sample_naver.text
soup = BeautifulSoup(naver_html, "html.parser")

titles = soup.select(".api_txt_lines.total_tit")
names = soup.select(".sub_txt.sub_name")

for result in zip(names,titles):
    print(type(result))
    print(result[0].text)
    print(result[1].text)
    print(result[1]['href'])
    print()

# api_txt_lines total_tit _cross_trigger


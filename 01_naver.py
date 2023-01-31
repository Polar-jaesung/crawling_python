import requests
from bs4 import BeautifulSoup

address ="http://naver.com"

window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

sample_naver= requests.get(address, headers=window_headers)

naver_html = sample_naver.text
soup = BeautifulSoup(naver_html, "html.parser")
naver_logo= soup.select_one(".logo_naver").text



print(sample_naver.request.headers)

# print(dir(sample_naver))
# print(naver_logo) 


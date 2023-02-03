import requests
from bs4 import BeautifulSoup

url ="https://www.coupang.com/np/search?component=&q="
window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
cookie = {"a": "b"}
#쿠팡에서는 쿠키값도 입력해줘야 크롤링 오류가 발생하지 않는다

keyword = input("검색할 상품은?")
search_url = url +keyword
req = requests.get(search_url,timeout=5, headers=window_headers, cookies=cookie)
html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select('[class=search-product]')

# for item in items:
#     print(item["class"])

print(len(items))





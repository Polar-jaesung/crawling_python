import requests
from bs4 import BeautifulSoup

url ="https://news.daum.net/"
window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=window_headers)
html = req.text

soup = BeautifulSoup(html, "html.parser")

articles = soup.select(".item_issue")

for article in articles:
    # 첫번째 방법
    '''company = article.select(".thumb_g")[1]['alt']'''
    # 두번째 방법(선생님은 이걸 선호)
    company = article.select_one(".logo_cp > img")['alt'] #언론사
    category = article.select_one(".txt_category") #카테고리
    title = article.select_one(".link_txt") 
    link = title['href']
    
    print(company)
    print(f"분야: {category.text}")
    print(f"제목: {title.text.strip()} // {link} ")
    print()
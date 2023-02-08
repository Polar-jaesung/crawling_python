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
items = soup.select(".api_ani_send")

rank_num=1
for area in items:    
    ad = area.select_one(".link_ad")
    if ad: 
        # print("광고입니다")
        continue 
        # continue사용하면 아래 코드는 실행x 위로 다시 돌아감

    print(f"<<{rank_num}>>")
    names = area.select_one(".sub_txt.sub_name")
    titles = area.select_one(".api_txt_lines.total_tit")    
    print(names.text)
    print(titles.text)
    print(titles['href'])
    print()

    rank_num+= 1



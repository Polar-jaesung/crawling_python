from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url ="https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword=input("검색어 입력하세요 : ")

url =base_url + keyword

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)
#page불러오는데 시간이 걸리므로 time을 자주 사용하게 된다 

'''
자바스크립트 기능을 사용해서 '스크롤'기능을 이용함. 현재 x축 이동은 필요없으므로 
y축 이동만 2000으로 설정해서 해봄 
document.body.scrollHeight사용하면 화면 가장 밑까지 스크롤 됨
반복문을 쓰면 스크롤을 몇번 반복할지 정할 수 있음
'''
for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)


naver_html = driver.page_source

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



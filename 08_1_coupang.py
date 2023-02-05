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

rank =1 
#rank를 이렇게 밖에 둘수도 있다 
for item in items:
    name = item.select_one(".name")
    rocket = item.select_one(".badge.rocket")
    price = item.select_one(".price-value")
    all_thumb = item.select_one(".search-product-wrap-img")
    thumb= all_thumb.get('data-img-src')
    # get을 쓰면 없는 단어는 none 으로 출력됨 (get안쓰면 에러로 뜸)

    '''첫번째 방법'''
    # all_link = item.select_one("a")
    # link = all_link["href"]
    '''두번째 방법'''
    # link = item.select_one("a")['href']
    '''세번째 방법'''
    link = item.a["href"]

    if not rocket:
        #조건문에서 not 을 처음 사용함
        continue 
        #continue 사용하면 다음 코드는 실행하지 말고! 다시 위로 올라가 라는 의미
    else:
        print(f"{rank}위")
        print(name.text)
        print(f"{price.text}원")
        print(f"https://www.coupang.com{link}")
        if thumb:
            img_url = f"https:{thumb}"
        else:
            img_url = f"https:{all_thumb['src']}" 
        print(img_url)
        print()

        img_req = requests.get(img_url)

        with open(f"08_coupang/{rank}.jpg", "wb") as f:
            f.write(img_req.content)
        rank += 1





import requests
from bs4 import BeautifulSoup

url ="http://naver.com"

window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=window_headers)
html = req.text
soup = BeautifulSoup(html, "html.parser")
'''
# 첫번째
print(soup.h1)
print('////')

# 두번째
h1= soup.find('h1')
print(h1)
print('////')

# 세번째
h1_select = soup.select_one('h1')
print(h1_select)
print('////')

# 네번째
h1_class = soup.find(class_="logo_default")
print(h1_class)
'''


'''
# (1) class를 통해 찾기 
nav = soup.find(class_="nav", string='증권')
print(nav)
print("=======")

# (2) tag를 통해 찾기 
nav_tag = soup.find("a", string='증권')
print(nav_tag)
'''

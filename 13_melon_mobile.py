from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#에러를 짧게 쓰기위해 이렇게 별도로 NoSuchElementException 지정함
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")
# options.add_argument("--start-maximized")
options.add_argument("window-size=500,1000")
options.add_experimental_option("detach",True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service, options=options)

url ="https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(1)

print(driver.current_url)

if driver.current_url != url:
    driver.get(url)
    time.sleep(1)

driver.find_element(By.LINK_TEXT,"멜론차트").click()
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR,"#moreBtn")[1].click()
time.sleep(1)

#1번째 방법
char_list = driver.find_element(By.CSS_SELECTOR,"#_chartList")
items = char_list.find_elements(By.CSS_SELECTOR,".list_item")

#2번째 방법
'''
items = driver.find_elements(By.CSS_SELECTOR,".list_item")
for item in items[:]:
    try:
        ranking = item.find_element(By.CSS_SELECTOR, ".ranking_num")
    except NoSuchElementException:
        print("랭크가 없으므로 삭제합니다")
        items.remove(item)
'''
#실제로 움직이는 효과를 보여주는 [액션체인]
action = ActionChains(driver)

for rank,item in enumerate(items[:10],1):
    action.move_to_element(item).perform()
    title= item.find_element(By.CSS_SELECTOR, ".title.ellipsis")
    name = item.find_element(By.CSS_SELECTOR, ".name.ellipsis")
    thumb = item.find_element(By.CSS_SELECTOR,".inner > span")
    thumb.click()
    time.sleep(1)
    album_url = driver.current_url
    #클릭하고 다시 뒤로 돌아오기
    driver.back()
    time.sleep(1)

    print(f"<<{rank}>>")
    print(title.text)
    print(name.text)
    print(f"앨범링크 :{album_url} ")
    print()

    time.sleep(1)

# action.move_to_element(items[90]).perform()

# print(len(items))
# driver.quit()
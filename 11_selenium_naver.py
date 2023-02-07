from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()

options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url ="https://naver.com"

driver.get(url)
time.sleep(2)

driver.find_element(By.ID, "query").send_keys("손흥민")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#search_btn").click()
time.sleep(2)

# driver.find_elements(By.CLASS_NAME,"menu")[4].click()
# time.sleep(2)

driver.find_element(By.XPATH, '//*[text()="VIEW"]').click()
time.sleep(2)

# driver.find_element(By.NAME,"query").clear()
# time.sleep(2)

# driver.find_element(By.NAME,"query").send_keys("리액트")
# time.sleep(2)

# driver.find_element(By.NAME,"query").send_keys(Keys.ENTER)
# time.sleep(2)

for i in range(5):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
    time.sleep(1)

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

driver.save_screenshot("11_selenium/naver.png")
print("스크린샷 저장 완료")

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach",True)

service = Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service=service, options=options)

url = "https://naver.com"
driver.get(url)
time.sleep(2)

'''
<input id="query" name="query" type="text" title="검색어 입력" maxlength="255" 
class="input_text" tabindex="1" accesskey="s" style="ime-mode:active;" 
autocomplete="off" placeholder="검색어를 입력해 주세요." 
onclick="document.getElementById('fbm').value=1;" value="" data-atcmp-element="">
'''

'''
#타이핑과 엔터를 한줄의 코드에 입력 가능
driver.find_element(By.XPATH,'//*[@title="검색어 입력"]').send_keys("리액트",Keys.ENTER)
time.sleep(2)

# driver.find_element(By.XPATH,'//*[@text="VIEW"]').click()
driver.find_element(By.LINK_TEXT,"VIEW").click()
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT, "인플루").click()
'''

navs = driver.find_elements(By.CLASS_NAME, "nav")

# print(navs)
# print()
# print(dir(navs[0]))
# print()
# print(len(navs))
for num,nav in enumerate(navs,1):
    # print(num)
    # print(nav.get_attribute("outerHTML"))
    '''outerHTML:해당 클래스를 감싸고 있는 HTML을 전부 보여준다 '''
    # print(nav.text)
    # print()
    if nav.text =="쇼핑":
        nav.click()
        break

time.sleep(2)

driver.quit()

'''
** 배울 find 문법
driver.find_element(By.CLASS_NAME)
driver.find_element(By.ID)
driver.find_element(By.CSS_SELECTOR)
driver.find_element(By.NAME)
driver.find_element(By.TAG_NAME)
driver.find_element(By.XPATH)
driver.find_element(By.LINK_TEXT)
driver.find_element(By.PARTIAL_LINK_TEXT)
'''
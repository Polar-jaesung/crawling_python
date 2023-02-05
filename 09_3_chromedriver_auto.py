from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

'''
위의 코드는 저장해두고 사용하자 Webdriver Manager를 사용해서 크롤 업데이트 마다
셀레니움을 자동 업데이트 해준다.
**전제조건은 첫 1회는 크롬드라이버를 직접 설치해줘야 한다 
'''

driver.get("https://www.google.com")
time.sleep(2)
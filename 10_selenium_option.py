from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/777.0.0.0 Safari/537.36"
user_data=r"/Users/JaeSung/Desktop/파이썬_크롤링/김플_인프런/10_selenium_option/jaesung"

options = Options()
#화면 꺼지지 않음
options.add_experimental_option("detach",True)

#user-agent 정보 변경
options.add_argument(f"user-agent={user_agent}")
#user_data 저장
options.add_argument(f"user-data-dir={user_data}")

#(1) 화면 크기 최대
options.add_argument("--start-maximized")
#브라우저가 풀스크린 모드(F11)로 실행됩니다.
# options.add_argument('--start-fullscreen')
#화면 크기 조절
# options.add_argument("window-size=500,500")
#브라우저에 음소거 옵션을 적용합니다.
options.add_argument('--mute-audio')
#시크릿 모드의 브라우저가 실행됩니다.
# options.add_argument('incognito') 
#화면창 안띄우고 작업하기
# options.add_argument("--headless")
#(2) 브라우저 맨위에 '자동화 중입니다'문구 삭제
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#(3) 터미널 불필요한 문구 삭제
options.add_experimental_option("excludeSwitches", ["enable-logging"])

#강사님이 주로 사용하는건 1,2,3

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url ="https://naver.com"

driver.get(url)
# print(driver.page_source[:1000])
# driver.quit()
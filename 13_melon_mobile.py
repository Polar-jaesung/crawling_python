from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

options.add_argument(f"user-agent={user_agent}")
options.add_argument("--start-maximized")
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

# driver.quit()
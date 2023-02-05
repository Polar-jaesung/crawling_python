from selenium import webdriver
import time 

url ="http://naver.com"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)

# title = driver.title

# print(title)

html = driver.page_source
# 글자수 500자로 제한해서 가져올때 
print(html[:500])
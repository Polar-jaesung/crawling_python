import requests
from bs4 import BeautifulSoup

url ="https://www.ssg.com/event/eventMain.ssg"
window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=window_headers)
html = req.text
soup = BeautifulSoup(html, "html.parser")

event_pages = soup.select_one(".evt_osmu_lst")
all_events= event_pages.select(".eo_link")

for event in all_events:
    link=event['href']
    if link.startswith("https"):
        print(link)
    else:
        print(f"https://www.ssg.com{link}")    
    contents = event.select_one(".eo_in")
    each_content = contents.find_all(string=True)

    for only_text in each_content:
        if only_text != "\n":  #/n이 아니다! 슬래쉬 구분 실수하지 않도록
            print(only_text)
    print()
import requests
from bs4 import BeautifulSoup

url ="https://www.melon.com/chart/index.htm"
window_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=window_headers)
html = req.text
soup = BeautifulSoup(html,"html.parser")

'''list_50=soup.select(".lst50")
list_100=soup.select(".lst100")

list_all=list_50+list_100'''

list_all = soup.select(".lst50,.lst100")

def get_song_nums(song_num_text):
    song_num = []
    for num in song_num_text:
        if num.isdigit():
            song_num.append(num)
    song_num= "".join(song_num)

    return song_num

for rank,i in enumerate(list_all,1):
    title= i.select_one(".ellipsis.rank01 a")
    
    singer = i.select_one(".ellipsis.rank02 > a")
    singer_link = get_song_nums(singer['href']) 

    album = i.select_one(".ellipsis.rank03 > a")
    # 자식 태그 가리킬 때는 '>' 입력해주면 된다
    album_link = get_song_nums(album['href']) 

    print(f"{rank}: {title.text}")
    print(f"{singer.text} /// https://www.melon.com/artist/timeline.htm?artistId={singer_link}")
    print(f"{album.text} /// https://www.melon.com/album/detail.htm?albumId={album_link}")
    

    print()

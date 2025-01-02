from bs4 import BeautifulSoup
import requests

url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
news = soup.find_all("a", class_="gPFEn")
icount = 1
for new in news:
    print("NO.", icount)
    print(new.text)
    print(new["href"], "\n")
    icount += 1

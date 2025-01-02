from bs4 import BeautifulSoup
import requests

google_url = ""

url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

news = soup.find_all("div", attrs={"class": "W8yrY"})

i_block_count = 1
for new in news:
    left_news = new.find("article", class_="IBr9hb")
    left_a = left_news.find("a", class_="gPFEn")
    left_time = left_news.find("time", class_="hvbAAd")

    print("Block NO.", i_block_count)
    print(left_a.text)
    print(left_a["href"])
    print(left_time["datetime"], "\n")
    i_block_count += 1
    right_news = new.find_all("article", class_="UwIKyb")
    for right_new in right_news:
        right_a = right_new.find("a", class_="gPFEn")
        right_time = right_new.find("time", class_="hvbAAd")
        print(right_a.text)
        print(right_a["href"])
        print(right_time["datetime"], "\n")
    print("\n")

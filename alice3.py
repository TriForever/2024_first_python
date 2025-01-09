from bs4 import BeautifulSoup
import requests
import pandas as pd
google_url = ""

url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# news = soup.find_all("div", attrs={"class": "W8yrY"})
topics = soup.find_all("div", attrs={"class": "W8yrY"})
# i_block_count = 1

list_of_news = list()

# for new in news:

#     mags = new.find_all("div", class_="vr1PYe")
#     titles = new.find_all("a", class_="gPFEn")
#     times = new.find_all("time", class_="hvbAAd")

#     for mag, title, time in zip(mags, titles, times):
#         print(mag.text)
#         print(title.text)
#         print(time["datetime"], "\n")

# left_news = new.find("article", class_="IBr9hb")
# left_a = left_news.find("a", class_="gPFEn")
# left_time = left_news.find("time", class_="hvbAAd")
# left_mag = left_news.find("div", class_="vr1PYe")

# print("Block NO.", i_block_count)
# print(left_mag.text)
# print(left_a.text)
# print(left_a["href"])
# print(left_time["datetime"], "\n")
# i_block_count += 1
# right_news = new.find_all("article", class_="UwIKyb")
# for right_new in right_news:
#     right_a = right_new.find("a", class_="gPFEn")
#     right_time = right_new.find("time", class_="hvbAAd")
#     right_mag = right_new.find("div", class_="vr1PYe")
#     print(right_mag.text)
#     print(right_a.text)
#     print(right_a["href"])
#     print(right_time["datetime"], "\n")
# print("\n")
for topic_index, topic in enumerate(topics):

    mags = topic.find_all("div", class_="vr1PYe")
    titles = topic.find_all("a", class_="gPFEn")
    times = topic.find_all("time", class_="hvbAAd")

    for mag, title, time in zip(mags, titles, times):

        print(mag.text)
        print(title.text)
        print(time["datetime"], "\n")

        list_of_news.append(
            {
                "topic_id": topic_index,
                "media": mag.text,
                "title": title.text,
                "url": "https://news.google.com"+title["href"][1:],
                "time": time["datetime"]
            })

df = pd.DataFrame(list_of_news)
df.to_csv("news.csv")

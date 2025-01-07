import requests
from bs4 import BeautifulSoup
url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"

res = requests.get(url)

# print(res) #Response 200 表示成功

# print(len(res.text))


soup = BeautifulSoup(res.text, 'html.parser')

topic_elements = soup.find_all("div", class_="W8yrY")

for topic_element in topic_elements:

    topic_titles = soup.find_all("a", class_="gPFEn")
    for topic_title in topic_titles:
        print(topic_title.text)
        print(topic_title["href"], "\n")
    # left_side = topic_element.find("a", class_="gPFEn")
    # print(left_side.text)
    # print(left_side["href"])

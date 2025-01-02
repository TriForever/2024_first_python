

from bs4 import BeautifulSoup
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())


print(soup.b)
print(soup.b.string)
print(soup.b.name)


x_find_p_with_story = soup.find("p", class_="story")
x_find_p_with_story = soup.find("p", attrs={"class": "story"})  # 與上面相同

print(x_find_p_with_story)

x_find_all = soup.find_all("a")
print(x_find_all)

for x in x_find_all:
    print(x)

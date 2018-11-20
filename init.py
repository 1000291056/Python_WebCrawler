from bs4 import BeautifulSoup
msg="hello \
the world!"
print(str(msg)[0:2])
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title title1"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,"html.parser")
for a_mark in soup.findAll("a"):
    print(a_mark.get("href"))
#print html content
#print(soup.get_text)
tag=soup.p
print(tag)
print(tag.string)
tag.string.replace_with("repalce_text")
print(tag.string)
print(type(tag.string))

print(type(tag))
print(tag["class"])
del tag["class"]
print(tag,end="\n *******************************\n")
#for content in soup.body.contents:

for content in soup.body.children:#dicrect node
    print(content)
print("**********************discendants******************")
#print(type(soup.body.discendants)
#for discendant in soup.head.discendants:
   #print(discendant)
print("**********************findAll******************")
for mTag in soup.findAll():
    print(mTag)

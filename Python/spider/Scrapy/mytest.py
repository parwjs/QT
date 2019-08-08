import requests

#requests完美解决编码问题
response = requests.get("https://book.jd.com/")
data = bytes(response.text,response.encoding).decode("gbk","ignore")

# s = [1,2,3,5]
# t = set(s)
# w = [{1:"al",2:"bl",3:"cl",5:"dl"}]
# x = 0
# for j in t:
#     l = w[x][j]
#     print(l)
# x += 1

# s = [1,23,5,6,0]
# r = ["adjka","dkasdj","as","ji","op"]
# alll = []
#
# for k in s:
#     for item in r:
#         alll.append({k:item})
# print(alll)

import urllib.request
from lxml import html
data = urllib.request.urlopen('https://list.jd.com/list.html?cat=1713,3281&page=130').read().decode('utf-8','ignore')
etree = html.etree
htmls = etree.HTML(data)
bookname = htmls.xpath("//div[@class='p-name']/a/em/text()")
print(bookname)




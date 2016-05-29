import urllib2
import bs4
import json

connect = urllib2.urlopen('https://zh.wikisource.org/zh-hant/%E5%AE%8B%E8%AF%8D%E4%B8%89%E7%99%BE%E9%A6%96')
page = connect.read()
content = bs4.BeautifulSoup(page, 'html.parser')

headers = content.find_all('h2')
bodys = content.find_all('div',  { "class": "poem" })

headers.remove(headers[0])
last = headers[len(headers) - 1]
headers.remove(last)

assert(len(headers) == len(bodys))

song300 = []

for header in headers:
	index = headers.index(header)
	body = bodys[index]

	title = header.find('b').get_text()
	author = header.find('a').get_text()
	content = body.find('p').get_text().split('\n')

	poem = {}
	poem['title'] = title
	poem['author'] = author
	poem['content'] = content
	song300.append(poem)

target = open('song300.json', 'w')
target.write(json.dumps(song300).decode('unicode-escape').encode('utf8'))
target.close()

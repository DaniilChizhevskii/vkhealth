import requests
import json
from lxml import html
from bs4 import BeautifulSoup
def get():
	r = requests.get('https://vk.com/dev/health')
	content = r.content
	soup = BeautifulSoup(content, 'html.parser')
	js = str(soup.body.find_all('script')[1])
	x = js.find('content')
	js = js[x+23:]
	y = js.find('};')
	js = js[:y]
	js = '[' + js
	js = js[:js.__len__()-77]
	js = json.loads(js)
	status = '{'
	for i in range(11):
		if (js[i][1].find('Работает') != -1):
			working = True
		else:
			working =  False
		status = status + '"' + js[i][0] + '":{"working":"' + str(working).lower() + '","ping":' + str(js[i][2]) + ',"uptime":' + str(js[i][3]) + '},'
	status = json.loads(status[:status.__len__()-1] + '}')
	return status
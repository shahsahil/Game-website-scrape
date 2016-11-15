import bs4
import requests
import csv
import webbrowser
from selenium import webdriver

def scrape(url):
	response = requests.get(url)
	html = response.content
	soup = bs4.BeautifulSoup(html, "html.parser")
	
	game = soup.find_all('div',attrs={'class':'backgroundGradientGrey boxShadow'})
	for i in game:
		name = i.find('h3').find('a')
		print(name.string);
		details = i.find('p', attrs = {'style':'text-align: justify;'})
		gdet = details.string
		gameurl = name['href']
		gurl = gameurl
		response = requests.get(gameurl)
		html = response.content
		soup2 = bs4.BeautifulSoup(html, "html.parser")
		image = soup2.find('img', attrs={'id':'frontCover'})
		image_url= 'http://thegamesdb.net'+ str(image['src'])
		gimg = image_url
		gamevitals = soup2.find('div', attrs={'id':'gameVitals'})
		allvitals = (gamevitals.find('p')).find_all('span', attrs={'class':'grey'})
		qq=[]
		for j in allvitals:
			qq.append(j.string)
		print(qq)
		vital = gamevitals.p
		for j in allvitals:
			gamevitals.span.decompose()
		a= vital.find_all('img')
		if a  !='None':
			for i in a:
				vital.img.decompose()
		#print(vital)
		for i in vital:
			try:
				vital.br.extract()
			except:
				pass
		r=[]
		for i in vital:
			x=i.nextSibling
			#
			if(x!='\n'):
				r.append(x)
		del r[-1]
		#print(r)
		rr=[]
		for x in r:
			x = x.replace(u'\xa0', u' ').strip()
			rr.append(x)
		print(rr)
		print("")
		
		print(id)

#generate all urls and then use the scrape function

c=0
'''
#pc
for i in range(1,64):
	try:
		st = 'http://thegamesdb.net/browse/1/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#xbox 360
for i in range(1,17):
	try:
		st = 'http://thegamesdb.net/browse/15/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
'''
#xbox one		
for i in range(1,4):
	try:
		st = 'http://thegamesdb.net/browse/4920/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
'''
#android
for i in range(1,5):
	try:
		st = 'http://thegamesdb.net/browse/4916/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#ios
for i in range(1,3):
	try:
		st = 'http://thegamesdb.net/browse/4915/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#ps2
for i in range(1,21):
	try:
		st = 'http://thegamesdb.net/browse/11/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#ps3
for i in range(1,18):
	try:
		st = 'http://thegamesdb.net/browse/12/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#ps4
for i in range(1,5):
	try:
		st = 'http://thegamesdb.net/browse/4919/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#psvita
for i in range(1,4):
	try:
		st = 'http://thegamesdb.net/browse/39/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#psp
for i in range(1,9):
	try:
		st = 'http://thegamesdb.net/browse/13/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#nintendo wii
for i in range(1,12):
	try:
		st = 'http://thegamesdb.net/browse/9/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#nintendo 64
for i in range(1,4):
	try:
		st = 'http://thegamesdb.net/browse/3/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass
#gameboy
for i in range(1,12):
	try:
		st = 'http://thegamesdb.net/browse/5/?sortBy=g.GameTitle&limit=100&searchview=listing&page='+str(i)
		scrape(st)
	except:
		c=c+1
		pass

'''				
print(c)
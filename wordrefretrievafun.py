# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import logging
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def webtest():
	url='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'
	r=requests.get(url)
	return r.content[300:340]



def synonyms(word):
	try:
		payload={'w':word,'dict':'essin'}
		page="http://www.wordreference.com/redirect/translation.aspx"
		#proxies={'http': '35.199.24.197:80'}
		
		s = requests.Session()
		r = s.get(page,params=payload)
		
		#r = requests.get(page,payload)
		
		
			
			
			#PARSING
		soup=BeautifulSoup(r.content,'html.parser')
		def has_li_and_no_span(tag):
			return tag.name=='li' and not bool(tag.span)
		
		
		
		target=soup.find_all('div',attrs={'class':'trans clickable'})[0]
		
		finaltarget=target.find_all(has_li_and_no_span)
		
		sins=[]
		for targ in finaltarget:
			sins.append(targ.get_text().encode('utf-8').split(','))
			indvsins=[]
		for cc in sins:
			for m in cc:
				indvsins.append(m)
	except Exception as e:
		logging.exception('message')
	return indvsins[random.randint(1,len(indvsins))-1]
	

	







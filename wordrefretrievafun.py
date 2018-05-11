# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random






def synonyms(word):
	payload={'w':word,'dict':'essin'}
	page="http://www.wordreference.com/redirect/translation.aspx"
	
	
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
	return indvsins[random.randint(1,len(indvsins))-1]
	

	







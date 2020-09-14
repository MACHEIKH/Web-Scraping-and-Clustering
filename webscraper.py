#Author: Amrita Reddy
#Description: This file create a web craper that is used to scrape article names from the PLOS ONE webpage 

import requests 
from bs4 import BeautifulSoup
import csv


f = csv.writer(open('Article_Names.csv', "w"))
f.writerow(["Article Title"])



def scraper(url, tag, attribute):
	"""Scrapes certain attributes from a webpage and writes the text to a file 

	inputs:
	url - webpage to be scraped 
	tag - html tag of elements to be found 
	atribute - attribute of element to be located 

	"""
	html = requests.get(url).text #uses the requests library to obtain the html from a webpage 

	soup = BeautifulSoup(html, "lxml") #creates a soup with the html from the webpage 
	articles = soup.find_all(tag, class_= attribute) #finds all instances with specified tag and attribute 

	for article in articles:
		f.writerow([article.get_text().strip()]) #writes the text into a csv file 


#scrapes news article names from 2000 pages of the journal PLOS ONE 
for i in range(0, 100):
	url = 'https://journals.plos.org/plosone/browse?resultView=cover&page=' + str(i)
	scraper(url, 'h2', 'title')

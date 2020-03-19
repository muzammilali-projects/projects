##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Sat Mar 14 02:21:02 2020
#
#@author: muzammilali
#"""
#import requests
#import bs4
#from bs4 import BeautifulSoup
#import pandas as pd
#import time
#
#max_results_per_city = 10
#
#city_set = ['New+York']#,'Chicago']#,'San+Francisco', 'Austin', 'Seattle', 'Los+Angeles', 'Philadelphia', 'Atlanta', 'Dallas', 'Pittsburgh', 'Portland', 'Phoenix', 'Denver', 'Houston', 'Miami', 'Washington+DC', 'Boulder']
#
#columns = ["city", "job_title", "company_name", "location", "summary"]
#
#sample_df = pd.DataFrame(columns = columns)
#
##scraping code:
#for city in city_set:
#  print(city)
#  for start in range(0, max_results_per_city, 1):
#      print(start)
#      page = requests.get('http://www.indeed.com/jobs?q=data+engineer&l=' + str(city) + '&start=' + str(start))
#      print('http://www.indeed.com/jobs?q=data+engineer&l=' + str(city) + '&start=' + str(start))
#      time.sleep(1)  #ensuring at least 1 second between page grabs
#      soup = BeautifulSoup(page.text, "lxml", from_encoding="utf-8")
#      for div in soup.find_all(name="div", attrs={"class":"jobsearch-SerpJobCard unifiedRow row result"}):
#        #print(div)
#        #specifying row num for index of job posting in dataframe
#        num = (len(sample_df) + 1) 
#        #creating an empty list to hold the data for each posting
#        job_post = [] 
#        #append city name
#        job_post.append(city) 
#        #grabbing job title
#        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
#          job_post.append(a["title"]) 
#          print(a["title"])
#        #grabbing company name
#        for b in div.find_all(name="span", attrs={"class":"company"}): 
#          job_post.append(b.text.strip()) 
#          print(b.text.strip())
#        #grabbing location name
#        for c in  div.findAll(name='span', attrs={'class': 'location'}): 
#          job_post.append(c.text.strip()) 
#          print(c.text.strip())
#        #grabbing summary text
#        for d in div.findAll(name='div', attrs={'class': 'summary'}):
#          job_post.append(d.text.strip()) 
#          print(d.text.strip())
#
#        sample_df.loc[num] = job_post
#
##saving sample_df as a local csv file — define your own local path to save contents 
#sample_df.to_csv("TEST.csv", encoding='utf-8')
#
#outF = open("test.txt", "w")
#outF.write(soup.prettify())
#outF.close()

from constants import variableX
print(variableX)
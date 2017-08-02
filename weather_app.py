# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import matplotlib as plt
import scrapy
import requests
import lxml 
from io import StringIO, BytesIO

today=(datetime.date.today()+datetime.timedelta(1)).isoformat()
tomorrow=(datetime.date.today()+datetime.timedelta(2)).isoformat()


'''rucsoft@gmail.com Rucsoft5^'''
class person:
    def __init__(self,email):
        self.email=email
        self.zipcodes=[]
        
    def add_location(self,zipcode):
        self.zipcodes.append(zipcode)
    
    def show_locations(self):
        print(self.zipcodes)

 
def create_zip(zip_array):
    useful_ziplist = ''
    for i in range(0,len(zip_array)):
        if i == len(zip_array)-1:
           useful_ziplist = useful_ziplist+str(zip_array[i])
        else:
            useful_ziplist= useful_ziplist + str(zip_array[i]) + '+'
    return useful_ziplist
'''
def get_weather_data(zip_array, today, tomorrow):
    str_zipcode= create_zip(zip_array)
    xml= 'http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?zipCodeList='+str_zipcode+'&product=time-series&begin=' + today + 'T00:00:00&end=' + tomorrow + 'T00:00:00&maxt=maxt&mint=mint&pop12=pop12'
    page = requests.get(xml)
    tree = lxml.etree.fromstring(page.content)
    for i in range(0, len(zip_array)):
        find_text = tree.xpath('//data/parameters['i']*')
        for j in range(0, len(find_text)):
            
'''
    

    
paul=person('ggg')
paul.add_location(70605)
paul.add_location(48316)
xml_zipcode = create_zip(paul.zipcodes)

xml= 'http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?zipCodeList='+xml_zipcode+'&product=time-series&begin=' + today + 'T00:00:00&end=' + tomorrow + 'T00:00:00&maxt=maxt&mint=mint&pop12=pop12'
page = requests.get(xml)

tree = lxml.etree.fromstring(page.content)
find_text = tree.xpath('//data/parameters[1]//*')
find_text3 = tree.xpath('//data/parameters[1]//value')
find_text2 = tree.xpath('//data/parameters[1]//name')

    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:29:49 2017

@author: stef
"""
import datetime
import matplotlib as plt
import scrapy

today=datetime.date.today().isoformat()
tomorrow=(datetime.date.today()+datetime.timedelta(1)).isoformat()

'''rucsoft@gmail.com Rucsoft5^'''
class person:
    def __init__(self,email):
        self.email=email
        self.locations=[]
        
    def add_location(self,location):
        self.locations.append(location)
    
    def show_locations(self):
        print(self.locations)
        
    def print_weather_data(self):
        for i in self.locations:
            print(i)
            print(i.weather_data)
        
class location:

    ziplist = []
    
    def __init__(self,zipcode):
        self.zipcode=zipcode
        self.ziplist.append(zipcode)
        
    def weather_data(self,weather_data):
        self.weather_data=weather_data
        
    def __repr__(self):
        return str(self.zipcode)
    
lake=location(70605)
paul=person('ggg')
paul.add_location(lake)
lake.weather_data(99)
    
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:21:07 2020

@author: Elliott Light
"""

# Raw input should have about 250 links.
# Final output should have about 118 links.

import pandas as pd
import os
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urljoin
import urllib.request
import re
import csv


os.chdir('D:\\Documents\\WGU\\C996') #changes the working directory to the specified path.
print(os.getcwd()) #prints the current working directory.

from_web_data = urllib.request.urlopen('https://www.census.gov/programs-surveys/popest.html').read() #Scrapes the website, in this case, the census.gov page. It's passed as a file-like object.
soupy = BeautifulSoup(from_web_data, 'html.parser') #creates a BS object and parses it as an lxml file.
type(soupy) #Checks the type of object we have, in this case, a BeautifulSoup object.
print(soupy.prettify()[:200]) #makes the document a little prettier/easier to read. Prints the first 200 characters so we can see if it worked.
atag = soupy.find_all('a') #Finds all of the a tags in our soup variable "soupy).

    
web_url = 'http://www.census.gov/' #starts our "seed" url
abs_url = [] #creates a list seed for the following loop.
for urls in atag:
   abs_url.append(urljoin(web_url, urls.get('href'))) #if the link is a relative link, it will append the base, "web_url"'s content to it, making it an absolute link.
   
abs_url = [s.strip('/') for s in abs_url] # Removes the trailing '/' from our abs_url list.

only_pages = [] # All anchors on the same page have a "#" in them. This loop will remove them.
for i in abs_url:
    flag = 0
    for elem in i:
        if elem == '#': #If the "#" is flagged.
            flag = 1 # This sets "flag" equal to 1, and it gets passed.
    if not flag: # If "flag" is not set off...
        only_pages.append(i) #The link gets put into our new list "only_pages".


unique_url = sorted(set(only_pages)) #gets all of the unique urls.

unique_url = pd.DataFrame({'Websites': unique_url}) #Converts the string to a panda's data frame. This will allow us to write it to a .csv file.
unique_url.to_csv('parsed_data.csv') #sends every unique link to this file.
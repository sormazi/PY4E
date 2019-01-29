from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context() #for https:// hosts to work in the program
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
position = int(input("Enter position: "))
count = int(input("Enter count: "))

for i in range(count):
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        URL = tag.get('href', None)
        s.append(URL) # get all the URLs into a list
        NAME = tag.text
        t.append(NAME) # get all the names into a list
    #printing list elements
    url = s[position-1] #we have to locate the number of the URL first before we can go furthur, removing this line will cause the program to look at one URL over and over again
    print ('Retrieving: ' + s[position-1]) #since numbering in python starts from 0, and the program wants us to start counting from 1, so we subtract 1 to reflect that in our solution

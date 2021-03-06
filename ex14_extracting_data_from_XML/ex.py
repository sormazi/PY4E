import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# extract all the comment/count values from the url and get the sum of all of them
url = input("Enter url: ")

# get the content of the url as a string
data = urllib.request.urlopen(url).read()

# transform the string content into a xml tree
tree = ET.fromstring(data)

# find all count elements
counts = tree.findall('comments/comment/count')

# extract the value of each count element and add it to the total
total = 0
for count in counts:
    total += int(count.text)

print('total: ',total)

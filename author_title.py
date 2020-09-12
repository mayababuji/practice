#!/usr/bin/python
#1) Copy paste the XMl data from the URL to a file books.xml
# https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms762271(v%3Dvs.85)
#2.Write a program to access the author name and title.
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
aut_dict = {}
for child in root.findall('book'):
    aut_dict[child.find('author').text] = child.find('title').text
print(aut_dict)



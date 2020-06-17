#!/usr/bin/python
#Python program to remove leading zeros from an IP address.

import re

def remove_leading_zero(ip):
    #\d Matches any decimal digit, this is equivalent to the set class [0-9].
    #Matches any decimal digit, this is equivalent to the set class [0-9].
    pattern = r'\b0+(\d)'
    string = re.sub(pattern,r'\1',ip)
    return string

if __name__ == '__main__':
    print(remove_leading_zero("001.200.1020.00400"))
    print(remove_leading_zero('10.0.01.10'))




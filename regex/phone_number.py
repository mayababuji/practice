#!/usr/bin/python
#find the phone number in a string 428-909-8484
import re
def find_phone_number(ph_num):
    '''
    Function to find if a given string has a valid phone number
    '''
    found_phone_number = False
    pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    for strng in ph_num.split():
        if pattern.search(strng):
            found_phone_number = True
    if found_phone_number is True:
        print("Found the phone number in the string which is {0}".format(strng))
    else:
        print("Did not find a valid phone number in the string")

if  __name__ == '__main__':
   find_phone_number('hi my number is 400-000-0000')
   find_phone_number('hi my number is 40000000')


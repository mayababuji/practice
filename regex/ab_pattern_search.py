#!/usr/bin/python
# Write a Python program that matches a string that has an a followed by zero or more b's
import re

def ab_pattern_search(test_string):
    '''
    Function to find the if a string has pattern like ab ,abb...
    '''
    # .* matches s followed by zero or more characters
    pattern = re.compile('ab.*')
    if pattern.search(test_string):
        print("Valid string {}".format(test_string))
    else:
        print("Invalid string {0}".format(test_string))

if __name__ == '__main__':
    ab_pattern_search('abb')
    ab_pattern_search('ddabb')
    ab_pattern_search('###abb')
    ab_pattern_search('pick')


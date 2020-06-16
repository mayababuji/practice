#!/usr/bin/python
# Write a Python program that matches a string that has an a followed by zero or more b's
#Write a Python program that matches a string that has an a followed by one or more b's.
import re

def zero_or_more_ab(test_string):
    '''
    Function that matches a string that has an a followed by zero or more b's
    '''
    # * matches ab followed by zero or more b character
    pattern = re.compile('ab*')
    if pattern.search(test_string):
        print("{} is valid string with 'a' followed by zero or more b's".format(test_string))
    else:
        print("{} is invalid string with 'a' not followed by zero or more b's".format(test_string))

def one_or_more_ab(test_string):
    '''
    Function that matches a string that has an a followed by one or more b's.
    '''
    # * matches ab followed by zero or more b character
    pattern = re.compile('ab+')
    if pattern.search(test_string):
        print("{} is valid string that has an 'a' followed by one or more b's ".format(test_string))
    else:
        print("{} is invalid string do not has an 'a' followed by one or more b's ".format(test_string))
if __name__ == '__main__':
    zero_or_more_ab('ac')
    zero_or_more_ab('ddabb')
    zero_or_more_ab('###abb')
    zero_or_more_ab('pick')
    zero_or_more_ab('abc')

    one_or_more_ab('ac')
    one_or_more_ab('abc')
    one_or_more_ab('abc')
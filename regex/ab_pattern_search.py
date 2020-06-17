#!/usr/bin/python
#Question source courtesy https://www.w3resource.com/python-exercises/re/
# Write a Python program that matches a string that has an a followed by zero or more b's
#Write a Python program that matches a string that has an a followed by one or more b's.
#Write a Python program that matches a string that has an a followed by three 'b'.
#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def zero_or_more_b(test_string):
    '''
    Function that matches a string that has an a followed by zero or more b's
    '''
    # * matches ab followed by zero or more b character
    pattern = re.compile('ab?')
    if pattern.search(test_string):
        print("{} is valid string with 'a' followed by zero or more b's".format(test_string))
    else:
        print("{} is invalid string with 'a' not followed by zero or more b's".format(test_string))

def one_or_more_b(test_string):
    '''
    Function that matches a string that has an a followed by one or more b's.
    '''
    # + matches ab followed by one or more b character
    pattern = re.compile('ab+')
    if pattern.search(test_string):
        print("{} is valid string that has an 'a' followed by one or more b's ".format(test_string))
    else:
        print("{} is invalid string do not has an 'a' followed by one or more b's ".format(test_string))

def three_or_more_b(test_string):
    '''
    Function that matches a string that has an a followed by two to three or more b's.
    '''
    # {2,3} matches a followed by 2 to 3 or more b character
    pattern = re.compile('ab{2,3}')
    if pattern.search(test_string):
        print("{} is valid string that has an 'a' followed by two to three or more b's ".format(test_string))
    else:
        print("{} is invalid string do not has an 'a' followed by two to three or more b's ".format(test_string))

def end_in_b(test_string):
    '''
    Function that matches a string that has an 'a' followed by anything, ending in 'b'.
    '''
    #  * matches 0 or more ,$ matches end of string
    pattern = re.compile('a*b$')
    if pattern.search(test_string):
        print("{} is valid string that has an 'a' ending in b ".format(test_string))
    else:
        print("{} is invalid string do not has an 'a' ending in b ".format(test_string))

if __name__ == '__main__':
    zero_or_more_b('ac')
    zero_or_more_b('ddabb')
    zero_or_more_b('###abb')
    zero_or_more_b('pick')
    zero_or_more_b('abc')

    one_or_more_b('ac')
    one_or_more_b('abc')
    one_or_more_b('abc')

    three_or_more_b('abb')
    three_or_more_b('#$%$abbbbbbbbbb')
    three_or_more_b('ab')

    end_in_b("###asnvfbbb")
    end_in_b("asnvfl")
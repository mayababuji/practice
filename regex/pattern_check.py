#!/usr/bin/python
#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
#use with and without re.compile and check the time taken for both

import re
import time
def check_pattern(test_strng):
    '''
    Function to if the string matches the pattern '[a-z0-9A-Z]'
    '''
    pattern = '[a-z0-9A-Z]'
    pattern_occurence = re.compile(pattern)
    if pattern_occurence.search(test_strng):
        print("Valid set of characters found in string {0}".format(test_strng))
    else:
        print("Invalid set of characters found in the string {0}".format(test_strng))

def check_pattern_without_recompile(test_strng):
    '''
    Function to if the string matches the pattern '[a-z0-9A-Z]' without using re.compile
    '''
    pattern = '[a-z0-9A-Z]'
    if re.search(pattern,test_strng):
        print("Valid set of characters found in string {0}".format(test_strng))
    else:
        print("Invalid set of characters found in the string {0}".format(test_strng))
if __name__ == '__main__':
    start_time = time.time()
    check_pattern('hello')
    check_pattern('@@@@@')
    end_time_1 = time.time() - start_time
    print('With compilation took {} seconds'.format(end_time_1))
    start = time.time()
    check_pattern_without_recompile('hello')
    check_pattern_without_recompile('@@@@@')
    end_time_2 = time.time() - start
    print('Without compilation took {} seconds'.format(end_time_2))
    print("With re.compile is {}% faster than without using re.compile".format(round(end_time_1/end_time_2)))

#result
# Valid set of characters found in string hello
# Invalid set of characters found in the string @@@@@
# With compilation took 0.0002799034118652344 seconds
# Valid set of characters found in string hello
# Invalid set of characters found in the string @@@@@
# Without compilation took 1.5020370483398438e-05 seconds
# With re.compile is 21% faster than without using re.compile
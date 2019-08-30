#Program to find the number  of a followed by zero in a string
import logging
logging.basicConfig(level=logging.INFO)
def occurence(strng_input):
    return strng_input.count('a0')
    
if __name__ == '__main__':
    result = occurence('mayaa0 isa0 n0 a1')
    logging.info("the number of occurence of a0 in the string is {0}".format(result))

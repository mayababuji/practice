#Program that accepts a sentence and calculate the number of upper case letters and lower case letters.
import logging
logging.basicConfig(level=logging.INFO)
def CountUpperLower(sentence):
    return sum(map(str.islower,sentence)), sum(map(str.isupper,sentence))
     
if __name__ == '__main__':
    lower_count , upper_count = CountUpperLower('Maa')
    logging.info("the count of LOWER CASE is {0} and UPPER CASE is {1}".format(lower_count , upper_count))

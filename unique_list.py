#Program to remove duplicate and return the length of the unique list and the unique list (eg a = [1,1,3,4] will return a = [1,3,4] and the length will be 3)
import logging
logging.basicConfig(level=logging.INFO)
def unique_list(val):
    return len(set(val)),set(val)
if __name__ == '__main__':
    length, unique_list = unique_list([1,1,3,4])
    logging.info('the length of the unique list is {0} and the unique list is {1}'.format(length,unique_list))

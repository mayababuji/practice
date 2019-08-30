#Program to check if a string is composed of all unique characters.eg func_unique("ajdkw") -- True  func_unique("hi how are you") -- False
import logging
logging.basicConfig(level=logging.INFO)

def IsUnique(string_input):
    char_list = []
    for i in string_input:
        if i in char_list:
            logging.info("the string is not unique")
            return False
        if not i.isspace():
            char_list.append(i)
    logging.info("the string is unique")
    return True
        #print(char_list) 
if __name__ == '__main__':
    result = IsUnique('hi how are you')
    print(result)

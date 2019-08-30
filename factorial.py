#find factorial of a value


import logging
logging.basicConfig(level=logging.INFO)

def fact(num):
    factorial = 1
    if num < 0:
        #LOG.info("Negative values does not have factorial")
        logging.info('This is an info message')
    elif num == 0 :
        return 0
    else:
        for i in range(1,num+1):
            factorial = factorial *i
        return factorial
print(fact(-1))

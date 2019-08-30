#Write a function to generate Fibinocci series

eg fib(5) = [1, 1, 2, 3, 5]

import logging
logging.basicConfig(level=logging.INFO)

def fib(num):
    a = 0
    b = 1
    c = []
    while b <= num:
        a, b = b , a+b
        c.append(a)
    return c
if __name__ == '__main__':
    result = fib(10)
    logging.info("The fibinocci series is {0}".format(result))
	

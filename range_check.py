#Assert a test case true if the input falls under the range[-5,5]
import logging
logging.basicConfig(level=logging.INFO)
def input_range(num):   
   try:    
       assert(num in range(-5,6))
       logging.info("the number falls under the range of [-5,5]")
   except:
       logging.info("the number does not fall under the range")
       return False
if __name__ == '__main__':
    a = input_range(5)
        

#!/usr/bin/python
#Function to validate ip adrress

import socket
address = input("the ip address:")
#Method 1 using the module socket
try:
    socket.inet_aton(address)
    print("The ip address is valid and is validated using the module socket")
except:
    socket.error
    print("The ip is invalid and is verified using the module socket ")
#Method 2 by looping in the adress and checking if it falls under the range 255
valid_address = True

if address.count('.') > 3:
    valid_address = False
for i in address.split('.'):
    if int(i) > 255:
        valid_address = False
if valid_address is False:
    print("The ip is invalid and verified by looping thru the address")
else:
    print("The ip is valid and verfied by looping thru the adress")



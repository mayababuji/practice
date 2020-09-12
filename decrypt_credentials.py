#!/usr/bin/python
#Function to encrpt and decrpt a password
import getpass
import base64
user_name = input("Enter the username:")
pass_word = getpass.getpass(prompt="Enter the password: ")
pwd = user_name + '.' +pass_word
print("the password is {0}".format(pwd))


def encrypt_password(pwd):
    encrpt_value = base64.b64encode(pwd.encode())
    return(encrpt_value)

def decrpt_password(pwd):
    decrpted_value = base64.b64decode(pwd.decode())
    return(decrpted_value)
a= encrypt_password(pwd)
print("the encrpted passpwrd is {0}".format(a))
b= decrpt_password(a)
print("the decrpted value is {0}".format(b))






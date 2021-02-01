#!/usr/bin/python

# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time
# the user asks for a new password. Include your run-time code in a main method.

import string
import random



def generate_password(password_length):

    password_character = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    password = []
    for i in range(password_length):
        password.append(random.choice(password_character))
    return("".join(password))

if __name__ == '__main__':
    password_length = int(input("Enter the desired length of password"))
    print(generate_password(password_length))





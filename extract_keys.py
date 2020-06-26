#!/usr/bin/python
#Extract all keys in a  dictionary using next

test_dict = {'Python':1,'is':2,'a':2,'programming':3,'language':4}
len_dict = len(test_dict)
key_is = []
test_dict=iter(test_dict)
for i in range(0,len_dict):
    key_is.append(next(test_dict))
print(key_is)
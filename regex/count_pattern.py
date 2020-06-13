#!usr/bin/python
#Write a regular expression to count the pattern "volume1 in data using regex
# data = ["/mnt/volume1/vol/img.img", "/mnt/volume1/val2.img", "/mnt/volume2/val1.img"]
# pattern = "volume1"
# result = {"volume1": 2}

import re
def count_pattern(data,pattern):
    'Function searches for the pattern volume1 and returns it count '
    volume_regex = re.compile(pattern)
    result = {}
    for i in data:
        if volume_regex.search(i):
            if pattern in result.keys():
                result[pattern] += 1
            else:
                result[pattern] = 1
    return result

if __name__ == '__main__':
     data = ["/mnt/volume1/vol/img.img", "/mnt/volume1/val2.img", "/mnt/volume2/val1.img"]
     pattern = "volume1"
     count_pattern = count_pattern(data,pattern)
     print(count_pattern)


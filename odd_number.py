#Demonstrate the use of lambda functions to solve the following use case
#  input_list = [1,2,3,4,5,6,7,8,9,10]
# output = [1,3,5,7,9]
input_list = [1,2,3,4,5,6,7,8,9,10]
output = input_list[::2]
print("the output with list slicing is {0}".format(output))
output = [i for i in input_list if i%2>0]
print("the output with odd method is {0}".format(output))

output = list(filter(lambda x: (x%2 != 0) , input_list))
print("the output with lambda function is {0}".format(output))


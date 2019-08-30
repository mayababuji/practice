#Print the nth value in a fibinocci series.eg 9th fibinocci value is 21 ([0,1,1,2,3,5,8,13,21])

def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("invalid input")
    elif n == 0:
        return a
    else:
        for i in range(2,n):
            c = a +b
            a = b
            b = c 
	return b

print(fib(9))

result = 21

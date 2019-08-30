#check if the number is prime

def check_prime(num):
    for i in range(2,num):
        if (num%i) == 0:
            print(num,"is not prime")
            print(i,"times",num//i, "is", num)
            break
        else:
            print(num ,"is prime")
            break
print(check_prime(400))

import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
num=int(input("Enter Number to check prime or not : "))
if is_prime(num):
    print("The number is prime")
else:
    print("The number is not prime")

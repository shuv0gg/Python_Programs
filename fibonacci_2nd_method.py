def fibonacci(x):
    a=0
    b=1
    for _ in range(x):
        print(a,end = " ")
        nextterm=a+b
        a=b
        b=nextterm

num=int(input("Enter number to find fibonacci series :"))
fibonacci(num)
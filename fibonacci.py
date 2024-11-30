def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

num=int(input("Enter number to find fibonacci series :"))
print(f"The fibonacci series of {num} is {fibonacci(num)} ")
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

num=int(input("Enter number to check even or odd : "))
print(f"The number {num} is ",even_odd(num))
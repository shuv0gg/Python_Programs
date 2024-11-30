import math
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

x=int(input("Enter first length : "))
y=int(input("Enter second length : "))
z=int(input("Enter third length : "))
print(f"The area of triangle is {triangle_area(x,y,z)}")
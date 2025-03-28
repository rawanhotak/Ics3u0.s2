""
name:rawan abdelbasit
date:28/3/2005
virables: a&b is odd or even
print("Welcome to the even and odd detector!")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a % 2 == 0:
    print(f"{a} is even.")
else:
    print(f"{a} is odd.")
if b % 2 == 0:
    print(f"{b} is even.")
else:
    print(f"{b} is odd.")
if (a % 2 == 0) or (b % 2 == 0):
    print("The product will be even.")
else:
    print("The product will be odd.")                

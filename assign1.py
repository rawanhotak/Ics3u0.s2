""
rawan abdelbasit
1091840
ICS3U
date:28/3/2005
virables: a&b is odd or even
#This program tells if two numbers are even or odd, then shows if their product will be even or odd
""
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

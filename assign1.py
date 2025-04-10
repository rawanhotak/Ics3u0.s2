"""
rawan abdelbasit
1091840
ICS3U
date:28/3/2005
virables: a&b is odd or even
#This program tells if two numbers are even or odd, then shows if their product will be even or odd
"""
print("Welcome to the even and odd detector!")# Greet the user and introduce the program
# Ask the user to input two numbers
a = int(input("Enter the first number: "))# Convert the first input to an integer
b = int(input("Enter the second number: "))# Convert the second input to an integer
# Check if the first number is even or odd
if a % 2 == 0: # If the remainder when divided by 2 is 0, it's even
    print(f"{a} is even.")# Print that the number is even
else: # If the remainder is not 0, it's odd
    print(f"{a} is odd.")# Print that the number is odd
# Check if the second number is even or odd
if b % 2 == 0:# If the remainder when divided by 2 is 0, it's even
    print(f"{b} is even.")   # Print that the number is even
else: # If the remainder is not 0, it's odd
    print(f"{b} is odd.")# Print that the number is odd
# Determine if the product of the two numbers will be even or odd
if (a % 2 == 0) or (b % 2 == 0): # If either number is even, the product will be even
    print("The product will be even.")# Inform the user the product will be even
else: # If both numbers are odd, the product will be odd
    print("The product will be odd.")#Inform the user the product will be odd                

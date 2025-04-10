"""
Rawan abdelbasit
1091840
ICS3U
Variables:cents — the total amount in cents.
quarters — the number of 25-cent coins.
dimes — the number of 10-cent coins.
nickels — the number of 5-cent coins.
pennies — the remaining cents that are less than 5, representing pennies
# This function takes a value in cents and prints the number of quarters, dimes, nickels, and pennies needed to make that amount
"""
# Check if the cents amount is greater than 100 and calculate the remaining cents after removing whole dollars
cent5s=int(input("please enter the value of cents:"))
if cents > 100:
     cents= cents%100# Get the remainder after dividing by 100 (removes the dollar part)
     # Calculate the number of quarters (25 cents) in the remaining amount
     quarters = cents// 25# Integer division to find how many quarters fit in the remaining cents
cents %=25 # Update the remaining cents after removing the quarters
# Calculate the number of dimes (10 cents) in the remaining amount
dimes = cents // 10 # Integer division to find how many dimes fit in the remaining cents
cents %=10# Update the remaining cents after removing the dime

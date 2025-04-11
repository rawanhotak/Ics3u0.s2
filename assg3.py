"""
rawan abdelbasit
1091840
ICS3U
Variable dictionary:
(secret-number ) the random number the player has to guess
(attempts) the number of guesses allowed(6)
(guess) the player's current guess.
(i) counts how many guesses the player has made.
#This program is a guessing game where you have 6 chances to guess a number between 1 and 100
"""
print("Hello! Welcome to the number guessing game!")# Introduction message
print("I am thinking of a number between 1 and 100.")# Instructions about the game
print(f"You have a maximum of six (6) tries.") # Informing the user about the number of attempts allowed
import random
secret_number = random.randint(1, 100)# Generate a random number between 1 and 100
attempts = 6 # Set the maximum number of attempts
for i in range (attempts): # Loop for each attempt
      guess = int(input(f"Guess #{i+1}: ")) # Ask for the user's guess and convert it to an integer
      if guess < secret_number:# Check if the guess is lower than the secret number
         print("higher!")# Prompt the user to guess higher
      elif guess> secret_number:# Check if the guess is higher than the secret number
           print("lower!")#Prompt the user to guess lower
      else:# If the guess is correct
           print("you guessed right!")#Inform the user they guessed correctly
           break # Exit the loop as the correct guess was made
if guess!= secret_number:#If the loop ends without guessing correctly
   print(f"sorry, you're out of gueeses! the number was {secret_number}.")#Inform the user of the correct number


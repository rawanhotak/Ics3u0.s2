"""
ICS3U
date:28/5/2025
word_list: stores the list of words to check for palindrome
virables:word_list: stores the list of words to check for palindrome
word: used in the loop to access each word from the list
i: used as an index in the loop to compare letters
Length: stores the number of characters in each word to help compare from both ends
"""
# List of words to check

word_list = ["racecar", "noon", "desk", "madam", "level", "store", "eye"]

# Function to check if a word is a palindrome

def is_palindrome(word):

    length = len(word)

    for i in range(length // 2):

        if word[i] != word[length - 1 - i]:

            return False

    return True

# Loop through the list and print whether each word is a palindrome

print("Palindrome program!")

for word in word_list:

    if is_palindrome(word):

        print(f"{word} is a palindrome")

    else:

        print(f"{word} is not a palindrome")

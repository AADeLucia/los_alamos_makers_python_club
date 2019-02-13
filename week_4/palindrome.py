"""
Created on Wed Feb  6 18:16:25 2019

Palindrome: a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run
Note: our function only checks if a single word is a palindrome, not a phrase

Wrote functions to accomplish the following:
1. Check if a string is a palindrome
2. Check if a user inputed string is a palindrome
3. Check for all palindromes in a file

@author: Alexandra DeLucia
"""
import re # this package is for regular expressions


def is_palindrome(word):
    """ Tests if a word is a palindrome """
    # Convert word to lowercase
    word = word.lower()

    # "I" or "a" is not a palindrome
    if len(word) <= 1:
        return False

    # Loop through word
    for i, char in enumerate(word):
        # Compare char to char in negative index
        if char != word[-1-i]:
            return False
    # Return true if loop finishes
    return True


def user_input_palindrome():
    # 1. Get input string from user
    user_string = input("Enter your palindrome: ")
    print("You entered", user_string)

    # 2. Test if string is a palindrome (symetrical)
    # 3. Output result to user
    if is_palindrome(user_string):
        print(user_string, "is a palindrome")
    else:
        print(user_string, "not is a palindrome")


def file_input_palindrome(filename):
    # 1. Open file and save content
    with open(filename, "r") as f:
        file_content = f.read()

    # 2. Remove symbols
    file_content = re.sub("[^\w]", " ", file_content)
    # This added extra spaces. Replace multiple spaces with a single space
    file_content = re.sub("(\s)+|(\n)+", " ", file_content)

    # 3. Split content into word array
    # Because of our space/newline replacment, all words are
    # separated by a single space
    words_in_file = file_content.split(" ")

    # 4. Print all palindromes
    for word in words_in_file:
        if is_palindrome(word):
            print(word)


if __name__ == "__main__":
    #file_input_palindrome("mary_oliver_summer_day.txt")
    file_input_palindrome("grimms_fairy_tales.txt")

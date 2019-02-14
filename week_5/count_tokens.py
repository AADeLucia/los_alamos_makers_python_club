"""
Write functions to accomplish the following:
1. Fill in tokenize_file
2. Fill in count_tokens_in_file
3. Run program with your favorite text

@author: Alexandra DeLucia
"""
import re


# 1. Define a function to split long text into a word list
# and sanitize for analysis
# "words" are called "tokens"
def tokenize_file(file):
    """
    Tokenizes a given file.
    
    "tokenizing" refers to stripping the symbols from a text, transforming
    all words to lower case, and separating them into a list.
    
    Parameters
    ----------
    file : path to a plain text file to tokenize
    
    Returns
    -------
    list : list of all tokens in file
    """
    # Open the file
    
    # Clean all symbols from the text
    # Hint: how did we clean the text for our palindrome method?
    # Remove symbols

    # This added extra spaces. Replace multiple spaces with a single space
    
    # Split content into word array
    # Because of our space/newline replacment, all words are
    # separated by a single space
    
    # Convert words to lower case
    # Use .lower() on each string in the list
    # Use a list comprehension to access each word
    
    # Return word list
    return


# 2. Define a function to count tokens
def count_tokens_in_file(file):
    """
    Parameters
    ----------
    file : path to a plain text file to count the tokens
    
    Returns
    -------
    dict : a dictionary of tokens and their counts {token: count}
    """
    # Convert file into a list of words using our 
    # tokenize_file method
    
    # Create a data structure to hold tokens and their counts
    # Which data structure would work best for this?
    
    # Loop through the token list and update token counts
    
    # Return token/count structure
    return


# Separate our main from the rest of the file
if __name__ == "__main__":
    # 1. Get the raw token counts
    token_counts_dict = count_tokens_in_file("mary_oliver_summer_day.txt")
    
    # 2. Answer the following questions
    
    # How many unique words are in the text?
    
    # What is the most popular word?
    
    
    
    
    
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
    # Open the file
    with open(file, "r") as f:
        file_content = f.read()
    
    # Clean all symbols from the text
    # Hint: how did we clean the text for our palindrome method?
    # Remove symbols
    file_content = re.sub("[^\w]", " ", file_content)
    # This added extra spaces. Replace multiple spaces with a single space
    file_content = re.sub("(\s)+|(\n)+", " ", file_content)
    
    # Split content into word array
    # Because of our space/newline replacment, all words are
    # separated by a single space
    tokens_in_file = file_content.split(" ")
    
    # Convert words to lower case
    tokens_in_file = [w.lower() for w in tokens_in_file]
    
    return tokens_in_file


# 2. Define a function to count tokens
def count_tokens_in_file(file):
    # Convert file into a list of words using our 
    # tokenize_file method
    token_list = tokenize_file(file)
    
    # Create a data structure to hold tokens and their counts
    # Which data structure would work best for this?
    token_count_dict = {}
    
    # Loop through the token list and update token counts
    for token in token_list:
        if token in token_count_dict:
            token_count_dict[token] += 1
        else:
            token_count_dict[token] = 1
    
    return token_count_dict


# Separate our main from the rest of the file
if __name__ == "__main__":
    # 1. Get the raw token counts
    token_counts_dict = count_tokens_in_file("mary_oliver_summer_day.txt")
    
    # 2. Answer the following questions
    
    # How many unique words are in the text?
    print("There are {} unique words in the text".format(len(token_counts_dict)))
    
    # What is the most popular word?
    # Method 1
    most_popular_word = ""
    greatest_count = 0
    for token, count in token_counts_dict.items():
        if count >= greatest_count:
            greatest_count = count
            most_popular_word = token
    print("The most popular word is {}, appearing {} times".format(most_popular_word, greatest_count))
    
    # Method 2
    sorted_tokens = sorted(token_counts_dict, key=token_counts_dict.get, reverse=True)
    most_popular_word = sorted_tokens[0]
    greatest_count = token_counts_dict[most_popular_word]
    print("The most popular word is {}, appearing {} times".format(most_popular_word, greatest_count))
    
    
    
    
    
    
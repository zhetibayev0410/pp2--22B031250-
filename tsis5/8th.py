#Write a Python program to split a string at uppercase letters.
import re

def split_string_at_uppercase(string):
    pattern = r'([A-Z][a-z]*)'
    substrings = re.findall(pattern, string)
    return substrings

string = 'SplitThisStringAtUpperCase'
substrings = split_string_at_uppercase(string)
print(substrings)

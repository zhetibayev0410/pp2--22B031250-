# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

def find_sequences(input_string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences

input_string = 'Run, Forrest, run'
sequences = find_sequences(input_string)
print(sequences)

import re

string = "The quick brown fox jumps over the lazy dog with an apple and a banana."
pattern = re.compile(r'a.*b$')
if pattern.search(string):
    print("Match found!")
else:
    print("Match not found.")

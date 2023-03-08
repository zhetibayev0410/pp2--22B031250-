import re

pattern = r'a(bb|bbb)'
test_strings = ['abb', 'abbb', 'acbb', 'abcbb']
for s in test_strings:
    if re.match(pattern, s):
        print(f"'{s}' matches the pattern")
    else:
        print(f"'{s}' does not match the pattern")

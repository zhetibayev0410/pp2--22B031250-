import re

pattern = r'a[b]*'
input_string = 'abbbbb'
match = re.search(pattern, input_string)
if match:
    print('Match found!')
else:
    print('Match not found.')

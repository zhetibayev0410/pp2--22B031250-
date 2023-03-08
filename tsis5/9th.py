import re

def insert_spaces(text):
    return re.sub(r'(?<=\w)([A-Z])', r' \1', text)

# Example usage
text = "HelloWorld HowAreYouToday?"
spaced_text = insert_spaces(text)
print(spaced_text)

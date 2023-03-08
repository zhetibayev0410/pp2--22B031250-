def replace_with_colon(string):
    return string.replace(" ", ":").replace(",", ":").replace(".", ":")

# example usage
original_string = "Hello, world. This is a sample string."
new_string = replace_with_colon(original_string)
print(new_string)

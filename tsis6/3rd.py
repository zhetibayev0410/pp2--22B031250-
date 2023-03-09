#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# example usage
string = "Hello, World!"
upper, lower = count_upper_lower(string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

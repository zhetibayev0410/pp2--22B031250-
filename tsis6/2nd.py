#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
    return all(t)

# Example usage:
my_tuple = (True, True, False)
print(all_true(my_tuple)) # False

my_tuple = (True, True, True)
print(all_true(my_tuple)) # True

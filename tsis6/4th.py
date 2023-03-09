#Write a Python program that invoke square root function after specific milliseconds.
import time
import math

num = int(input("Enter a number: "))
delay = int(input("Enter a delay time in milliseconds: "))

time.sleep(delay/1000.0) # convert milliseconds to seconds

result = math.sqrt(num)

print("Square root of", num, "after", delay, "milliseconds is", result)

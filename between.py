import random
from math import floor
try:
	minimum = float(input("Enter minimum number? "))
	maximum = float(input("Enter maximum number? "))
except ValueError:
	print("One of your numbers weren't.. numbers")

print("Calculating medium")
medium = 0
match random.randint(1,2):
	case 1:
		print("Using method 1")
		medium = maximum - minimum
		medium = medium / 2
		medium = medium + minimum
	case 2:
		print("Using method 2")
		medium = maximum / 2
		medium = (minimum / 2) + medium
	case _:
		print("wattesigma")
print(f"Medium is: {medium}")

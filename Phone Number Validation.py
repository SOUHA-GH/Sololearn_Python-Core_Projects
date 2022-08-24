#The problem checks whether phone number has exactly 8 digits and starts with 1, 8 or 9, or not.
Output "Valid" if the number is valid and "Invalid", if it is not.
import re
pattern = r"^[189][0-9]{7}$"
#^ is for the number to start with [189], composed of the [0-9] digits, and {7} is the number of repetiations of a digit, to have exactly 8 digits.
$ to end total of [189] + [0-9]{7} which is equals to 8.
if re.match(pattern, input()):
    print("Valid")
else:
    print("Invalid")

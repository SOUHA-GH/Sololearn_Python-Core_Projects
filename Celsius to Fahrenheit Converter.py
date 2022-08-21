#The program gives a function that takes the Celsius value as an argument and returns the corresponding Fahrenheit value.
celsius = int(input())

def conv(c):
    fahrenheit=9/5 * c + 32
    return fahrenheit

fahrenheit = conv(celsius)
print(fahrenheit)

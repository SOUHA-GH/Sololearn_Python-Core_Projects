'''The program takes N (variable num in code template) positive numbers as input, 
and recursively calculates and outputs the first N numbers of the Fibonacci sequence (starting from 0).'''
num = int(input())
def Fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))
for i in range(num):
    print(Fibonacci(i))

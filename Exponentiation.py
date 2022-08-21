#The program calculates the sum that will result from doubling two choices 30 times to understand which one results in a larger amount.
a=1000000
b=0.01
for i in range(0,31):
    c=a*(2**i)
    d=b*(2**i)
if c<d:
    print(c)
else:
    print(d)

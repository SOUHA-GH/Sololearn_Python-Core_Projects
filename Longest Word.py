#Given a text as input, the program finds and outputs the longest word.
txt = input()
l=txt.split(' ')
maxi=' '
for i in l:
    for j in l:
        if len(i)<len(j):
            maxi=j
            break
print(maxi)

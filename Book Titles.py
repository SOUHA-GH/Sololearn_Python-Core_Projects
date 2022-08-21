'''The program makes a special book categorization system, which assigns each book from the provided file books.txt, a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.'''
file = open("/usercode/files/books.txt", "r")
books=file.readlines() 
for i in books:
    if i != books[-1]:
        print(i[0]+str(len(i)-1))
    else:
        print(i[0]+str(len(i)))
file.close()

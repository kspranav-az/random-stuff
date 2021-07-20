first=input(str("your first name :"))
middle=input(str("your middle name :"))
last=input(str("your last name :"))

A=first[0]
B=middle[0]

print("your name is", last, end=' ')
print( A, "\b.", end='')
print(B, "\b.", end='')

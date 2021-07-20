even=[]
odd=[]
for i in range(1,11,1):
    num=int(input("number"))
    if (num%2==0):
        even.append(num)
    else:
        odd.append(num)
print("all the even numbers are following:")
for x in range(len(even)):
    print(x)
print("all the odd numbers are following:")
for y in range(len(odd)):
    print(y)


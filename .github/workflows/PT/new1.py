even=[]
odd=[]
for i in range(1,11,1):
    num=int(input("number"))
    if (num%2==0):
        even.append(num)
    else:
        odd.append(num)
print("number of odd numbers are:",len(odd))
print("number of even numbers are:",len(even))


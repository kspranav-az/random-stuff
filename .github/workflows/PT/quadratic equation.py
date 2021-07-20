import math
print("enter the equation")
a=float(input("enter the cofficient of X^2 :"))
b=float(input("enter the cofficient of X^1 :"))
c=float(input("enter the constant term :"))

B=b**2
A=4*a*c
D=B-A

if(D>0):
    d=math.sqrt(D)
    x=(-b+d)/(2*a)
    y=(-b-d)/(2*a)
    print("the roots are")
    print(x,y)
elif(D==0):
    x=-b/(2*a)
    print("the roots are")
    print(x,x)
else:
    print("the roots are complex")
    x=complex(-b+D)
    print(x)
       

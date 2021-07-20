import math

print("Just put '-1' in place of unknown values.")
p=float(input("principal amount :"))
t=float(input("time period :"))
r=float(input("rate :"))
si=float(input("simple intrest :"))
P=p
T=t
R=r
SI=si

if(P==-1):
    P=(si*100)/(r*t)
    print(si,"rupees")
elif(R==-1):
    R=(si*100)/(p*t)
    print(R,"%")
elif(T==-1):
    T=(si*100)/(p*r)
    print(T,"years")
else:
    SI=(p*r*t)/100
    print(SI,"rupees")

    
         
        

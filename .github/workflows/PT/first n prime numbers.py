e=int(input("number:"))
for i in range(1,e+1):
    if(i>1):
        for n in range(2,i):
            if(i%n)==0:
                break
        else:
            print(i)


            

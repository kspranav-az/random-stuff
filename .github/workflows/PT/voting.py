print("welcome voter")
name = input("your name:")
age = int(input("your age:"))
if (age >= 18):
    print("sure", name, " you can vote")
    print("thankyou")
elif (age < 0):
    print("please use valid quantity")
else:
    print("sorry", name, " you can not vote")
    print("wait for", 18 - age, "years")




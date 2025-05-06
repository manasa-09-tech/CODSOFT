import random
a=[]
for i in range(33,123):
    a.append(chr(i))
b=int(input("enter the desired password length"))
c=int(input("enter how many  passwords do you want? "))
for j in range(0,c):
    d=""
    for k in range(0,b):
        d=d+random.choice(a)
    print(d,"\n")
    

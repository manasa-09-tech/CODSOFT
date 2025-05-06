import string
import random
a=int(input("enter the desired password length"))
b=int(input("enter how many  passwords do you want?"))
c=string.ascii_letters+string.digits+string.punctuation
for i in range(0,b):
    d=""
    for j in range(0,a):
        d=d+random.choice(c)
    print(d,"\n")
    

    
    

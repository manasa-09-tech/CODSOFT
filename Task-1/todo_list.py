print("***********************TO DO LIST***********************")
a=[]
b=[]
print(" 1,show all the task ","\n","2,insert the task ","\n","3,update the task","\n","4,update completed tasks","\n","5,pending tasks","\n","6,completed tasks","\n","7,exit from to-do-list")
j=1
while(j<=3):
    i=int(input(" enter your choice:-"))
    if(i==1):
        print(" your assigned tasks","\n",a)
        print(" ")
        continue
    elif(i==2):
        k=input(" enter a task:-")
        a.append(k)
        print(" Task Added","\n"," ")
        continue
    elif(i==3):
         l=input(" please enter a name of your updation with")
         n=a.index(l)
         a.remove(l)
         m=input(" enter your updation task")
         a.insert(n,m)
         print(" Task Updated","\n"," ")
         continue
    elif(i==4):
        w=input(" enter the task that you have completed")
        b.append(w)
        print(" ")
        continue
    elif(i==5):
        print(" incomplete task ")
        c=a
        for x in b:
            if(x in a):
                 c.remove(x)
        print(" ",c)
        print(" ")
        continue
    elif(i==6):
        print(" completed tasks")
        print(" ",b)
        print(" ")
        continue
    elif(i>=8):
        print(" entered a wrong number..retry please")
        print(" ")
        continue
    elif(i==7):
        print(" thankyou for your inputs...have a nice day ahead!")
        j=4

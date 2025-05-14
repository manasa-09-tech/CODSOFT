print("********************************************* Welcome to Contact Book! *********************************************","\n  ")
print(" 1. Add Contact","\n","2. View Contact List","\n","3. Search Contact","\n","4. Update Contact","\n","5. Delete Contact","\n","6. Exit","\n")
b=[]
i=0
while(i<3):
        print(" ")
        a=int(input(" enter your Choice"))
        print(" ")
        if(a==1):
                for j in range(1,2):
                        name=input(" Enter name:")
                        number=int(input(" Enter phone number:"))
                        email=input(" Enter email:") 
                        address=input(" Enter address:")
                        c=[]
                        for j in range(1,2):
                            c.append(name)
                            c.append(number)
                            c.append(email)
                            c.append(address)
                        b.append(c)
                print(" >>contact added successufully",c)
                print(" ")
                continue
        elif(a==2):
            print(" View Contact List","\n ")
            l=[" Name: "," Number: "," Email: "," Address: "]
            if(len(b)==0):
                print(" >>Empty Contacts List")
            else:
                for i in range(0,len(b)):
                    print(" >>The contact number",i+1,":")
                    for j in range(0,len(b[i])):
                        print("  ",l[j],b[i][j])
                    print(" ")
                print(" ")
                continue
        elif(a==3):
             x=input(" enter a name that you wanted to search for")
             y=0
             print(" ")
             for i in range(0,len(b)):
                 for j in range(0,1):
                     if(x==b[i][j]):
                         print("","name:",b[i][j],"\n"," phone number:",b[i][j+1])
                         y=1
                         
             if(y==0):
                 print(" >>No contact found")
        elif(a==4):
            if(len(b)==0):
                print(" >>Empty Contacts List")
            else:
             n=0
             print( " Update Contact")
             w=input(" Enter a name ")
             t=int(input(" Enter a phonenumber "))
             for i in range(0,len(b)):
                        for j in range(0,1):
                            if(b[i][j]==w and b[i][j+1]==t):
                                l=[" Name: "," Number: "," Email: "," Address: "]
                                print(" The current Details")
                                n=1
                                for x in range(0,1):
                                    for y in range(0,len(b[i])):
                                        print("  ",l[y],b[i][y])
                                        z=i
                                name=input(" Enter nameto update:")
                                number=int(input(" Enter phone number to update:"))
                                email=input(" Enter email to update:") 
                                address=input(" Enter address to update:")
                                for h in range(z,z+1):
                                               for k in range(0,1):
                                                              b[h][k]=name
                                                              b[h][k+1]=number
                                                              b[h][k+2]=email
                                                              b[h][k+3]=address
                                print(" >>Successfully Updated")
            if(n!=1):
                    print(" >>No Contact Found") 
                                                              
        elif(a==5):
            if(len(b)==0):
                    print(" >>Empty Contacts List")
            else:
                    y=input(" enter a name of the contact that you  wanted to delete")
                    x=int(input(" enter the contact number that you  wanted to delete"))
                    print(" ")
                    k=0
                    for i in range(0,len(b)):
                        for j in range(0,1):
                            if(b[i][j]==y and b[i][j+1]==x ):
                                y=i
                                k=1
                    if(k!=1):
                        print(" >>You Entered Contact is not available")
                    else:
                        z=b.pop(y)
                        print(" >>The contact was successfully deleted",z)
        elif(a==6):
            print(" >>Thankyou for visiting Contact Book!!")
            i=4


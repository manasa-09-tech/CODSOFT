import random
print("********************WELCOME TO ROCK-PAPER-SCISSORS GAME********************")
print(" Game Rules:","\n","  1.each round contains five chances")
print("   2.The one wins when""\n","     >> Rock beats scissor","\n","     >> scissor beats paper","\n","     >> paper beats rock")
print("   3.It becomes tie  when""\n","     >> Both Bot and you had a same choice","\n")
a=["Rock","Paper","Scissor"]
c={1:"Rock",2:"Paper",3:"Scissor"}
bot=0
you=0
print("choose","\n","   1 for Rock","\n","   2 for Paper","\n","   3 for Scissor","\n")
y=0
while(y<10):
        for j in range(0,5):
                x=random.choice(a)
                y=int(input("\n enter your choice"))
                if(y==1 or y==2 or y==3):
                            b=c.get(y)
                            if((x=="Rock" and b=="Rock") or (x=="Paper" and b=="Paper") or (x=="Scissor" and b=="Scissor")):
                                print(" The choice of bot is",x)
                                print(" OOPS!!,it's tie")
                            elif((x=="Rock" and b=="Scissor") or (x=="Scissor" and b=="Paper") or (x=="Paper" and b=="Rock")):
                                bot=bot+1
                                print(" The choice of bot is",x)
                                print(" Bot WON")
                            elif((b=="Rock" and x=="Scissor") or (b=="Scissor" and x=="Paper") or (b=="Paper" and x=="Rock")):
                                you=you+1
                                print(" The choice of bot is",x)
                                print(" You WON")
                else:
                    print(" you have entered a wrong choice,retry")
        print(" ")
        z=input(" Do you want to play again?(yes/no)")
        print(" ")
        if (z=="yes"):
            y=y+1
        else:
            print(" Thanks for playing")
            y=11
            
print(" ")
if(bot>you):
    print(" OOPS!!you Lost,The overall score is : ",bot,",bot won this round")
elif(bot==you):
    print(" OOPS!!, this round is tie")
else:
     print(" Hureyy!! The overall score is : ",you,",you won this round")
        
        



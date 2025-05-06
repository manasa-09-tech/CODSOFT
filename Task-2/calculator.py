import operations
a=int(input("enter a value"))
b=int(input("enter b value"))
print(" 1,Addition","\n","2,Subtraction","\n","3,multiplication","\n","4,division(quotient)","\n","5,Modulus(remainder)","\n","6,Exponentiation(power)","\n","7,Floor division","\n","8,Exit")
v=0
while(v<2):
    c=int(input(" enter your choice"))
    if(c==8):
        print(" Thankyou!!")
        v=2
    else:
      d=operations.op(a,b,c)
      print(" The result is:",d)

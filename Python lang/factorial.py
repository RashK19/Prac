a=int(input("enter a number= "))
fac=1
if(a>0):
    for i in range (1,a+1):
        fac=fac*i
    print("factorial of",a,"is",fac)
elif(a==0):
    print("factorial of 0 is 1")
else:
    print("invalid input")    
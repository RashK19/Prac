n=int(input("Enter a number in binary form= "))
s=str(n)
l=len(s)
sum=0
while(n>=0 and l>0):
    l=l-1
    #print("l=",l)
    div=int(n/10**l)
    #print("div=",div)
    sum=sum+(div*(2**l))
    #print("sum=",sum)
    n=int(n%(10**l))
    #print("n=",n)
print("In decimal form= ",sum)

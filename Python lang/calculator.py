while(1>0):
    print("1. addition")
    print("2. subtraction")
    print("3. multuplication")
    print("4. division(float)")
    print("5. division(floor)")
    print("6. modulus")
    print("7. power")
    print("8. exit")
    print("enter your choice= ")
    ch=int(input())
    if(ch==8):
        exit()
    elif(ch>=1 and ch<=7):
        a=int(input("enter first number= "))
        b=int(input("enter second number= "))
        if(ch==1):
            print(a+b)
        elif(ch==2):
            print(a-b)
        elif(ch==3):
            print(a*b)
        elif(ch==4):
            print(a/b)
        elif(ch==5):
            print(a//b)
        elif(ch==6):
            print(a%b)
        else:
            print(a**b)
    else:
        print("wrong choice")
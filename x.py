def add(a,b):
    sum=a+b
    print(sum)


def sub(a,b):
    sub=a-b
    print(sub)

def mul(a,b):
    mul=a*b
    print(mul)

def div(a,b):
    div=a/b
    if b==0:
        print("division is not possible")
    else:
        print(div)

choice=int(input("Enter the operation"))
if choice==1:
    add(5,6)
elif choice==2:
    sub(11,5)
elif choice==3:
    mul(1,2)
else:
    choice==4
    div(2,4)
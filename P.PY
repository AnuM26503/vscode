
def add():
    a=float(input("Enter the number"))
    b=float(input("Enter the number"))
    sum=a+b
    print(sum)


def sub():
    a=float(input("Enter the number"))
    b=float(input("Enter the number"))
    sub=a-b
    print(sub)

def mul():
    a=float(input("Enter the number"))
    b=float(input("Enter the number"))
    mul=a*b
    print(mul)

def div():
    a=float(input("Enter the number"))
    b=float(input("Enter the number"))
    div=a/b
    if b==0:
        print("division is not possible")
    else:
        print(div)

choice=int(input("Enter the operation"))
if choice==1:
    add()
elif choice==2:
    sub()
elif choice==3:
    mul()
else:
    choice==4
    div()
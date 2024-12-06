f=lambda a:a*a
k=f(5)
print(k)


def is_multiple3(n):
    return n%3==0
nums=[3,6,4,5]
multiple=list(filter(is_multiple3,nums))
print(multiple)


nums=[3,5,7,9,2]
multiple=list(filter(lambda n:n%3==0,nums))
print(multiple)

def add_all(a,b):
    return a+b
nums=[3,6,9,2]
even=list(filter(lambda n:n%2==0,nums))
double=list(map(lambda n:n*2,even))
sum=(add_all,double)
print(double)

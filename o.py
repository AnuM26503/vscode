l=[1,2,3,4,5]
a=dict(map(lambda n:(n,n*2),l))
print(a)


l=[1,2,3,4,5]
a={k:(lambda x:x*2)(k )for k in l}
print(a)



def below_20(n):
    return n<20
prices=[15,25,10,30,50]
new=list(filter(below_20,prices))
print(new)



customers=["Rahul","Antony","Salman","Arun","Kiran"]
a=list(filter(lambda x:x.startswith("A"),customers))
print(a)

customers=["Rahul","Antony","Salman","Arun","Kiran"]
a=[i for i in customers if 'A' in i[0]]
print(a)

customers=["Rahul","Antony","Salman","Arun","Kiran"]
new=[]
for customer in customers:
    if 'A' in customer[0]:
        new.append(customers)
print(new)
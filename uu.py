employees={'Antony':55000,'Susan':45000,'Kiran':60000}
new={}
for name,salary in employees.items():
    if salary>50000:
        new[name]='high'
    else:
        new[name]='low'
print(new)
words=['apple','banana','apple','orange','banana','apple']
new_words=set(words)
a={i:words.count(i)for i in new_words}
print(a)

y=10
def inner():
    x=4
    global y
    y=y+1
    print("x:",x)
inner()
print("y:",y)






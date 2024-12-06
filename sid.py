u=(input("ENTER YOUR USERNAME:"))
x=u.isalnum()
a=len(u)
if x==True:
   if a>15:
      print("Length Exceeded")
   elif a<6:
     print("Length Receded")
   else:
      print("validated")  
else:
   print("username is invalid")
      






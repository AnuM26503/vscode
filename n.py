a=int(input("Enter your body weight:"))
b=float(input("Enter your heightin m:"))
def BMI(a,b):
    BMI=a/(b*b)
    return BMI
bmi_call=(BMI(a,b))
print(bmi_call)

print("Enter marks:")
p=int(input("Physics:"))
ch=int(input("Chemistry:"))
b=int(input("Biology:"))
m=int(input("Math:"))
c=int(input("Computer:"))
avg=(p+ch+b+m+c)/5
if(avg>=90):
    print("Grade A")
elif(avg>=80):
    print("Grade B")
elif(avg>=70):
    print("Grade C")
elif(avg>=60):
    print("Grade D")
elif(avg>=40):
    print("Grade E")
else:
    print("Grade F")
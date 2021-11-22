sum= 0
unit = int (input())
if(unit <=50):
    sum= unit*0.50
elif(unit >50 and unit <=100):
    sum = unit*0.75
elif(unit>100 and unit<=250):
    sum = unit*1.20
else:
    sum =unit*1.50
print (sum)
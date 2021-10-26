users=["Aayush","Daiveek","Bhau","Jeetu"]
password =[1002,2536,9658,2331]
accounts=[101,102,103,104]
bal=[10200,20000,35200,23500]
acc=int(input("Account no. "))
pas=int(input("Password: "))
if(pas==password[accounts.index(acc)]):
    amnt=int(input("Enter Amount: "))
    accbal=accounts.index(acc)
    if(bal[accbal]<amnt):
        print("Insufficient Balance")
    else:
        print("Amount Deducted : ",amnt)
        bal[accbal]-=amnt
        print("Available amount: ",bal[accbal])
else:
    print("Incorrect Password")
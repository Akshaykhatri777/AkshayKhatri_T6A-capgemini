age = eval(input('Enter Age:'))
income = eval(input('Enter Income:'))
creditScore = eval(input('Enter Credit Score:'))
if age>18:
    if income >= 21000:
        if creditScore >= 700:
            print("Approved")
        else:
            print("Loan Rejected-Low Credit")
    else:
        print("Loan Rejected-Low Income")
else:
    print("Loan Rejected-Age not Eligible")
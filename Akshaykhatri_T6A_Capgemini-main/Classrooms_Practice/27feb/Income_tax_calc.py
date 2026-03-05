income = float(input("Enter annual income: "))

if income > 500000:
    if income <= 1000000:
        tax = income * 0.20
    else:
        tax = income * 0.30
else:
    if income > 250000:
        tax = income * 0.05
    else:
        tax = 0

print("Tax Amount:", tax)

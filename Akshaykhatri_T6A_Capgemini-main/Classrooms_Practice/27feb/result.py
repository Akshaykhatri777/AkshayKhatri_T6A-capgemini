maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 40:
    if science >= 40:
        if english >= 40:
            average = (maths + science + english) / 3
            
            if average >= 75:
                print("Result: Distinction")
            else:
                print("Result: Pass")
        else:
            print("Result: Fail")
    else:
        print("Result: Fail")
else:
    print("Result: Fail")

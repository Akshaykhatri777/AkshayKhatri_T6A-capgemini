age=int(input('enter ur age: '))
inc=int(input('enter income: '))
cs=int(input('enter ur credit score: '))
if(age>=21):
    if(inc>=25000):
        if(cs>=700):
            print('Load Approved')
        else:
            print('Load rejected(low credit score')
    else:
        print('Loan rejected(Low income)')
else:
    print('Loan rejected(Age npt eligible')

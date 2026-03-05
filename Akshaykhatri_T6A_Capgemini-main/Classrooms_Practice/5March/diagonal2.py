r=int(input('enter rows: '))
c=int(input('enter columns: '))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i+j==r+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()


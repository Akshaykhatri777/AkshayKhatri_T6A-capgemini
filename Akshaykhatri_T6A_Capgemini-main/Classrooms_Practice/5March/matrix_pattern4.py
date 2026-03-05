r=int(input('enter rows: '))
c=int(input('enter columns: '))
for i in range(1,r+1):
    for j in range(1,c+1):
        if i==1 and j==1 :
            print('* ',end='')
        elif i+j==r+1:
            print('# ',end='')
        elif i==r and j==c:
            print('@ ',end='')
        else:
            print('  ',end='')
    print()

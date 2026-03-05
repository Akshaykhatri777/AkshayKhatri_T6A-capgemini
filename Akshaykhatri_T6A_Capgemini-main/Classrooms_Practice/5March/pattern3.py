#r=int(input('enter rows: '))
#c=int(input('enter columns: '))
for i in range(0,5):
    for j in range(0,5):
        if i==j:
            print('*',end='')
        elif i>j:
            print('#',end='')
        else:
            print('@',end='')
    print()


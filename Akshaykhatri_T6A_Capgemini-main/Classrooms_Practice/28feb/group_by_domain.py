n=int(input('enter total elementes: '))
print('enter elements')
l=[]
while n>0:
    a=input()
    l.append(a)
    n-=1
d1={}
for i in l:
    l1=i.split('.')
    if l1[1] in d1:
        d1[l1[1]].append(l1[0])
    else:
        d1[l1[1]]=[l1[0]]
            
print(d1)
    

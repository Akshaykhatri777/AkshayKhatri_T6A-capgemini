l=[(2+3j),12,'Program','Python',False]
d1={}
for i in l:
    if type(i)!=str:
        continue
    for j in i:
        if j in 'aeiouAEIOU':
            if i in d1:
                d1[i]+=j
            else:
                d1[i]=j
print(d1)

l = [(2+3j),12,'Program','Python',False]  #op- {'Program':'oa','python':'o'}
d = {}
for i in l:
    if type(i)==str:
        v=''
        for j in i:
            if j in 'aeiouAEIOU':
                v+=j
        d[i]=v
print(d)

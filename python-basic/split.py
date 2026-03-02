l = ['p1.py','first.txt','t3.py','TK.txt','TF.com']
d = {}
for i in l:
    t=i.split(".")
    if t[1] in d:
        d[t[1]].append(t[0])
    else:
        d[t[1]]=[t[0]]
print(d)

# def findidx(val,*t):                           #tuple packing or single packing
#     print(t)
#     for i in range(len(t)):
#         if t[i]==val:
#             return i
# ans = findidx(50,10,20,30,40,50,60)
# print(ans)


def findidx(val,**t):
    return t
print(findidx(50,a='50',b=20,c=30,d=40,e=50,f=60))

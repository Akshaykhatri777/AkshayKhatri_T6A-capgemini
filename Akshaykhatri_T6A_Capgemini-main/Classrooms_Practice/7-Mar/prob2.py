# def sumofnum(*l):
#     sum=0
#     if 1<len(l)<6:
#         for i in l:
#             sum=sum+i
#     else:
#         return "Invalid"
#     return sum
# ans = sumofnum(*eval(input()))
# print(ans)


def sumofnum(l):
    summ=0
    if 1<len(l)<6:
        summ = sum(l)
    else:
        return "Invalid"
    return summ
ans = sumofnum(eval(input()))
print(ans)
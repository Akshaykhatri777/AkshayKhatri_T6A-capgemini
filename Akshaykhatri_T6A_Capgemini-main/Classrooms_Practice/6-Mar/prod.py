def prodlist():
    l = eval(input())
    prod = 1
    for i in l:
        prod = prod * i
    return prod
ans = prodlist()
print(ans)
def findlet():
    name = input()
    char = input()
    for i in range(len(name)):
        if name[i]==char:
            return i

ans = findlet()
print(ans)
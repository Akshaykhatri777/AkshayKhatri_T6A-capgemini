# import sys
# sys.setrecursionlimit(1500)
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
ans = fact(int(input()))
print(ans)
s1=input('enter: ')
l1=[s1[0]]
cnt=1
ans=''
n=len(s1)
for i in range(0,n-1):
    if s1[i]==s1[i+1]:
        cnt+=1
    else:
        ans+=s1[i]+str(cnt)
        cnt=1
ans += s1[n-1] + str(cnt)
print(ans)

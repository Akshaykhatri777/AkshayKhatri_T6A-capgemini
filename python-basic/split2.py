s = 'aaabbaaccc'
res = ''
count=1
for i in range(len(s)):
    if i<len(s)-1 and s[i]==s[i+1]:
        count+=1
    else:
        res+=s[i]+str(count)
        count=1
print(res)

# i = 0
# while i < len(s):
#     cnt = 1
#     while i + 1 < len(s) and s[i] == s[i + 1]:
#         cnt += 1
#         i += 1
#     res += s[i] + str(cnt)
#     i += 1
# print(res)
    
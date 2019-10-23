s = input()
cnt = 1
former = s[0] 
res = ''
for i in range(1, len(s)):
    if s[i] == former:
        former = s[i]
        cnt += 1
    else:
        res += former + str(cnt)
        former = s[i]
        cnt = 1
    if i == len(s) - 1:
        res += former + str(cnt)
print(res)

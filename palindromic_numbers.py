# 条件より絶対5桁
A, B = map(int, input().split())

cnt = 0

for i in  range(A, B+1):
    num = i
    res = []
    res_append = res.append
    while num > 0:
        q, mod = divmod(num, 10)
        res_append(mod)
        num = q
    if (res[0] == res[-1]) and (res[1] == res[-2]):
        cnt += 1

print(cnt)

N = int(input())

tnum = 0
iter_num = 0

for i in range(N):
    res = 0
    num = i+1
    while num % 2 == 0:
        num /= 2
        res += 1
    if iter_num <= res:
        iter_num = res
        tnum = i+1

print(tnum)

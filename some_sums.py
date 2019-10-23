N, A, B = map(int, input().split())

num_sum = 0
for i in range(N+1):
    res = 0
    num = i
    while num > 0:
        q, mod = divmod(num, 10)
        res += mod
        num = q
    if (res >= A) and (res <= B):
        num_sum += i

print(num_sum)

N = int(input())

min_res = 100000

for i in range(N):
    A = i+1
    B = N - A

    if (B >= 2) and (B < N):
        res = 0
        a_num = A
        b_num = B
        while a_num > 0:
            q, mod = divmod(a_num, 10)
            res += mod
            a_num = q
        while b_num > 0:
            q, mod = divmod(b_num, 10)
            res += mod
            b_num = q
        if min_res > res:
            min_res = res

print(min_res)

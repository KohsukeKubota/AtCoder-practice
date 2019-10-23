K, S = map(int, input().split())

res = 0

for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            three_sum = i + j + k
            if S == three_sum:
                res += 1

print(res)

N = int(input())
W_list = list(map(int, input().split()))

res = 200

for i in range(1, N):
    S1 = sum(W_list[:i+1])
    S2 = sum(W_list[i+1:])
    abs_val = abs(S1-S2)
    if abs_val < res:
        res = abs_val

print(res)

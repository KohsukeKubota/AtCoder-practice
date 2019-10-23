N = int(input())
K = int(input())
res = 1  
for i in range(res, N+1):
    if res*2 >= res+K:
        res = res+K
    else:
        res = res*2
print(res)

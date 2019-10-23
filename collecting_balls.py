N = int(input())
K = int(input())
X = list(map(int, input().split()))
res = 0
for x in X:
    if abs(x-K) >= abs(x):
        res += abs(x)*2
    else:
        res += abs(x-K)*2
print(res)

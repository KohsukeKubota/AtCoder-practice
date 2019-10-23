n = int(input())
A = list(map(int, input().split()))
res = 0
for a in A:
    while a % 2 != 1 or a % 3 == 2:
        a -= 1
        res += 1
print(res)

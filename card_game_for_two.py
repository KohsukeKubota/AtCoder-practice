N = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)

res = 0

for i in range(N):
    if i % 2 == 0:
        res += a_list[i]
    if i % 2 == 1:
        res -= a_list[i]

print(res)

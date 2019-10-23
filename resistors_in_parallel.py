N = int(input())
A_list = list(map(int, input().split()))

res = 0

for a in A_list:
    res += 1/a

print(1/res)

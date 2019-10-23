N = int(input())

a_list = list(map(int, input().split()))

max_num = -1
min_num = 10000000000

for i in range(N):
    num = a_list[i]
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(max_num - min_num)

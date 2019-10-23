A_list = list(map(int, input().split()))
A_list.sort(reverse=True)

print((A_list[0] * 10 + A_list[1]) + A_list[2])

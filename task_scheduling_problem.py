A_list = list(map(int, input().split()))
A_list_sorted = sorted(A_list)

print(0 + abs(A_list_sorted[1] - A_list_sorted[0]) + abs(A_list_sorted[2] - A_list_sorted[1]))

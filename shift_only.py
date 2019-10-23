N = int(input())
a_list = list(map(int, input().split()))
b_list = [int(a % 2) for a in a_list]
zero_list = [0 for a in a_list]
i = 0
while zero_list == b_list:
    a_list = [int(a / 2) for a in a_list]
    b_list = [int(a % 2) for a in a_list]
    i += 1
print(i)

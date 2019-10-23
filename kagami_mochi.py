N = int(input())
d_list = [int(input()) for i in range(N)]

num_dict = {}

for i in d_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

print(len(num_dict))

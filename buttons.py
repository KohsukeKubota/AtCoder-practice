A, B = map(int, input().split())

num_list = [A, B]
first_num = max(num_list)
first_choice_index = num_list.index(first_num)
num_list[first_choice_index] = num_list[first_choice_index] - 1
second_num = max(num_list)

print(first_num + second_num)

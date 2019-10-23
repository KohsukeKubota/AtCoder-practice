x, y = map(int, input().split())

first_group = [1, 3, 5, 7, 8, 10, 12]
second_group = [4, 6, 9, 11]

if x == 2 or y == 2:
    print('No')
elif x in first_group and y in second_group:
    print('No')
elif x in second_group and y in first_group:
    print('No')
else:
    print('Yes')

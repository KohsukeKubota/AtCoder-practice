S = input()

max_num = 0
continuous_num = 0

for s in S:
    if s == 'A' or s == 'C' or s == 'G' or s == 'T':
        continuous_num += 1
        if continuous_num > max_num:
            max_num = continuous_num
    else:
        continuous_num = 0

print(max_num)

S = input()

res = 1000

for i in range(len(S)-2):
    part_num = int(S[i:i+3])
    diff_num = abs(753 - part_num)
    if res > diff_num:
        res = diff_num

print(res)

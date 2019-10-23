A = list(map(int, input().split()))
five_cnt = 0
seven_cnt = 0

for a in A:
    if a == 5:
        five_cnt += 1
    elif a == 7:
        seven_cnt += 1

if five_cnt == 2 and seven_cnt == 1:
    print('YES')
else:
    print('NO')

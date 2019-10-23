S = input()

a_cnt = 0
b_cnt = 0
c_cnt = 0

for s in S:
    if s == 'a':
        a_cnt += 1
    elif s == 'b':
        b_cnt += 1
    elif s == 'c':
        c_cnt += 1

if a_cnt == 1 and b_cnt == 1 and c_cnt == 1:
    print('Yes')
else:
    print('No')

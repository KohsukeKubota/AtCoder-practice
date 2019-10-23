S = input()
S_reverse = S[::-1]

str_list = ['dream', 'dreamer', 'erase', 'eraser']
str_reverse_list = [s[::-1] for s in str_list]

can = True
print(len(S))
for i in range(len(S)):
    print(i)
    can2 = False
    for j in range(len(str_list)):
        d = str_reverse_list[j]
        if S_reverse[:i+1] == d:
            print('Hello')
            can2 = True
            i += len(d)
    if not (can2):
        can = False
        break

if (can):
    print('YES')
else:
    print('NO')

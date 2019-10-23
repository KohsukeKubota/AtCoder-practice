C1 = input()
C2 = input()
C3 = input()

s_list = []

for i, C in enumerate([C1, C2, C3]):
    s_list.append(C[i])

print(''.join(s_list))

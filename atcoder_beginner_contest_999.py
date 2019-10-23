n = input()

s_list = []

for i in range(len(n)):
    if n[i] == '9':
        s_list.append('1')
    elif n[i] == '1':
        s_list.append('9')
    else:
        s_list.append(n[i])

print(s_list[0] + s_list[1] + s_list[2])

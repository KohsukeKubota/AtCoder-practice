s = input()

aidx_list = []
zidx_list = []

for i in range(len(s)):
    if (s[i]  == 'A'):
        aidx_list.append(i)
    if (s[i] == 'Z'):
        zidx_list.append(i)

print(len(s[aidx_list[0]:zidx_list[-1]+1]))

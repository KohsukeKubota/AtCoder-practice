S = input()

num_dict = {}

for i in range(len(S)):
    if S[i] in num_dict:
        num_dict[S[i]] += 1
    else:
        num_dict[S[i]] = 1

if len(num_dict) == 2 and \
    len([i for i, x in enumerate(num_dict.values()) if x == 2]):
    print('Yes')
else:
    print('No')

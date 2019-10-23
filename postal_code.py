import sys
A, B = map(int, input().split())
S = input()
for i in range(len(S)):
    if i == A:
        if S[i] != '-':
            print('No')
            sys.exit()
    else:
        if S[i].isdigit() is False:
            print('No')
            sys.exit()
print('Yes')

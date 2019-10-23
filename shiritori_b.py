import sys


N = int(input())
W = [input() for _ in range(N)]

for i in range(1, N):
    if W[i] in W[:i]:
        print('No')
        sys.exit()
    else:
        if W[i][0] != W[i-1][-1]:
            print('No')
            sys.exit()
print('Yes')

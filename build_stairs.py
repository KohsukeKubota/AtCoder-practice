import sys
N = int(input())
H = list(map(int, input().split()))
if N == 1:
    print('Yes')
else:
    for i in reversed(range(N-1)):
        if H[i] -H[i+1] > 1: print('No');sys.exit()
        elif H[i] - H[i+1] == 1: H[i] -= 1
        else: continue
    print('Yes')

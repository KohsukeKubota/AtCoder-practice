import sys
N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))
set_ = set([a, b])
for p in P:
    if p in set_:
        print('NO')
        sys.exit()
    else:
        set_.add(p)
print('YES')

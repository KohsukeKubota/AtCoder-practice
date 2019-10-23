N = int(input())
A = [int(input()) for _ in range(N)]
set_ = set()
res = 0
for a in A:
    if a in set_:
        res += 1
    else:
        set_.add(a)
print(res)

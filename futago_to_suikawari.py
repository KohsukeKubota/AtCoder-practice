N, A, B = map(int, input().split())
SD = [input().split() for _ in range(N)]
res = 0
for s, d in SD:
    d = int(d)
    if A<= d <=B: dist = d
    elif d < A: dist = A
    else: dist = B
    if s == 'East': res += dist
    else: res -= dist
if res > 0: print('East {}'.format(res))
elif res < 0: print('West {}'.format(abs(res)))
else: print(0)

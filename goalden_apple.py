N, D = map(int, input().split())

width = 2*D + 1
q, mod = divmod(N, width)

if mod == 0:
    print(q)
else:
    print(q+1)

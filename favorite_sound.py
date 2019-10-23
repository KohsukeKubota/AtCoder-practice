A, B, C = map(int, input().split())

q = B // A

if q <= C:
    print(q)
else:
    print(C)

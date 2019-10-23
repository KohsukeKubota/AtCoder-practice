N, M, X = map(int, input().split())
A = list(map(int, input().split()))
to_zero = sum([1 for a in A if a < X])
to_n = sum([1 for a in A if a > X])
if to_zero >= to_n:
    print(to_n)
else:
    print(to_zero)

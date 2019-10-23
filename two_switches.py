A, B, C, D = map(int, input().split())
if C<=B<=D:
    if A<C: print(B-C)
    else: print(B-A)
elif A<=D<=B:
    if C<A: print(D-A)
    else: print(D-C)
else:
    print(0)

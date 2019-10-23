A, B, C, K = map(int, input().split())
S, T =  map(int, input().split())

if K <= S+T:
    print(S*A+T*B-(S+T)*C)
else:
    print(S*A+T*B)

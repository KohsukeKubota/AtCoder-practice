A, B, C = map(int, input().split())
X = A*B*C
while X >= (10**9+7):
    X %= (10**9+7)
else:
    X %= 10**9+7
print(X)

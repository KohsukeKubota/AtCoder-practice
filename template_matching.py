N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
for i in range(N-M+1):
    for j in range(N-M+1):
        print(i, j)
        print(A[i][j:j+M])

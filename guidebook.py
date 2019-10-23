N = int(input())
# input().split()をi+1と前後させると挙動が変化する
X = [[input().split(), i + 1] for i in range(N)]
X_sorted = sorted(X, key=lambda x: (x[0][0], -int(x[0][1])))

for x in X_sorted:
    print(x[1])

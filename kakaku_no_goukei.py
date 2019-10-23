n, X = map(int, input().split())
A = list(map(int, input().split()))
q = 10000
bin_X = ''
while q > 0:
    q, mod = divmod(X, 2)
    X = q
    bin_X = str(mod) + bin_X
if n - len(bin_X) > 0: bin_X = '0' + bin_X
res = 0
bin_X = bin_X[::-1]
for i in range(len(bin_X)):
    if bin_X[i] == '1':
        res += A[i]
print(res)

N = int(input())
S = input()
x = 0
res = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    if res < x:
        res = x
print(res)

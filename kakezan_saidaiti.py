A = int(input())

res = 0
for i in range(int(A/2)+1):
    x, y = A-i, i
    if res < x*y:
        res = x*y
print(res)

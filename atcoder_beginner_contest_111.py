import sys


N = int(input())

for i in range(N, 1000):
    c1 = i // 100
    c2 = (i-c1*100) // 10
    c3 = (i-c1*100-c2*10)
    if c1 == c2 == c3:
        print(i)
        sys.exit()

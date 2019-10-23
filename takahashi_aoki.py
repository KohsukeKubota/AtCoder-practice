import sys
a, b, n = int(input()), int(input()), int(input())
for i in range(n, 1000000):
    if (i % a == 0) and (i % b == 0):
        print(i)
        sys.exit()

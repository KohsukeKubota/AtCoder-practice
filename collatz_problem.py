import sys


s = int(input())
A = [0, s]

for i in range(2, 1000001):
    n = A[i-1]
    if n % 2 == 0:
        tmp = n / 2
        if tmp in A:
            print(i)
            sys.exit()
        else:
            A.append(tmp)
    else:
        tmp = 3 * n + 1
        if tmp in A:
            print(i)
            sys.exit()
        else:
            A.append(tmp)

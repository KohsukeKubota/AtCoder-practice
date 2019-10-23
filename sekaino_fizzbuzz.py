import sys

N = input()

if int(N) % 3 == 0:
    print('YES')
    sys.exit()

for i in range(len(N)):
    if N[i] == '3':
        print('YES')
        sys.exit()
print('NO')

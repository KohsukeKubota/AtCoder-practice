import sys
N = int(input())
S = input()
res = 'b'
if res == S:
    print(0)
    sys.exit()
else:
    for n in range(1, N+1):
        if n % 3 == 1: res = 'a' + res + 'c'
        elif n % 3 == 2: res = 'c' + res + 'a'
        else: res = 'b' + res + 'b'
        if res == S:
            print(n)
            sys.exit()
print(-1)

import sys
X = input()
set_ = set(['c', 'h', 'o', 'k', 'u'])
for i in range(len(X)):
    if X[i] in set_:
        if X[i] == 'c':
            if i < len(X)-1 and X[i+1] == 'h': continue
            else: print('NO'); sys.exit()
        elif X[i] == 'h':
            if X[i-1] == 'c': continue
            else: print('NO'); sys.exit()
    else: print('NO'); sys.exit()
print('YES')

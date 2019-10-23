import sys
w = input()
for s in set(w):
    if w.count(s) % 2 == 1:
        print('No')
        sys.exit()
print('Yes')

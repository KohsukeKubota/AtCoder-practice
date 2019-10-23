import sys
S = input()
T = input()
set_ = set(['a', 't', 'c', 'o', 'd', 'e', 'r', '@'])
for s, t in zip(S, T):
    if s in set_ and t == '@': continue
    elif s == '@' and t in set_: continue
    elif s == t: continue
    else: print('You will lose'); sys.exit()
print('You can win')

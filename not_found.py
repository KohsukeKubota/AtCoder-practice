import sys
S = input()
s_el = set(S)
for a in range(97, 97+26):
    if chr(a) not in s_el:
        print(chr(a))
        sys.exit()
print('None')

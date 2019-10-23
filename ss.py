import sys
S = input()
S = S[:-1]
for _ in range(len(S)):
    len_s = len(S)
    if len_s%2 == 0:
        s1 = S[:int(len_s/2)]
        s2 = S[int(len_s/2):len_s]
        if s1 == s2:
            print(len_s)
            sys.exit()
        else:
            S = S[:-1]
    else:
        S = S[:-1]

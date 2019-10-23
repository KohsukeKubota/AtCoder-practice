S = input()

cnt = 0

if S[0] != 'A':
    print('WA')
else:
    for i, s in enumerate(S[2:-1]):
        if s == 'C':
            cnt += 1
            c_idx = i
    if cnt == 1:
        c_idx += 2
        part_str = S[1:c_idx] + S[c_idx+1:]
        if part_str.islower():
            print('AC')
        else:
            print('WA')
    else:
        print('WA')

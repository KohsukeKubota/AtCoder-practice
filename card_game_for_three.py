S = [input() for _ in range(3)]
idx = 0
while len(S[idx]) > 0:
    card = S[idx][0]
    S[idx] = S[idx][1:]
    if card == 'a':
        idx = 0
    elif card == 'b':
        idx = 1
    else:
        idx = 2
if idx == 0:
    print('A')
elif idx == 1:
    print('B')
else:
    print('C')

A, B, C = map(int, input().split())
plus, minus = A+B, A-B
if plus != C and minus != C:
    print('!')
else:
    if plus == C and minus == C:
        print('?')
    elif plus == C and minus != C:
        print('+')
    elif plus != C and minus == C:
        print('-')

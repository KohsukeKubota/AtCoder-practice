N = input()

digit_sums = sum([int(n) for n in N])
if int(N) % digit_sums == 0:
    print('Yes')
else:
    print('No')

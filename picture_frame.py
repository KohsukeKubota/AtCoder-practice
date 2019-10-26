H, W = map(int, input().split())
A = [list(input().split()) for _ in range(H)]
for i in range(H+2):
    if i == 0 or i == H+1:
        print(''.join(['#'] * (W+2)))
    else:
        print(''.join(['#'] + A[i-1] + ['#']))

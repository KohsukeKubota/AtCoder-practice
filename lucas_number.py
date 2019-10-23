N = int(input())
L_forward = 2
L_backward = 1
if N == 1:
    print(L_backward)
else:
    for i in range(2, N+1):
        L = L_forward + L_backward
        L_forward = L_backward
        L_backward = L
    print(L)

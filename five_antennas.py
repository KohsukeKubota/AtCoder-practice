import numpy as np

N = 5
A = np.array([int(input()) for i in range(N)])
k = int(input())

xx, yy = np.meshgrid(A, A)
comb = np.c_[xx.flatten(), yy.flatten()]

diff_ = np.abs(comb[:, 0] - comb[:, 1])
max_diff = np.max(diff_)

if max_diff <= k:
    print('Yay!')
else:
    print(':(')


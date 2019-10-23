import numpy as np
H, W = map(int, input().split())
S = [input() for _ in range(H)]
res = np.zeros((H, W), dtype=np.int32)
for i in range(H):
    str_ = S[i]
    for j in range(W):
        if str_[j] == '#':
            res[i-1][j-1] += 1
            res[i][j-1] += 1
            res[i+1][j-1] += 1
            res[i-1][j] += 1
            res[i+1][j] += 1
            res[i-1][j+1] += 1
            res[i][j+1] += 1
            res[i+1][j+1] += 1
for i in range(H):
    tmp_list = ['#' if v == 0 else str(v) for v in res[i][:]]
    print(''.join(tmp_list))

import numpy as np


N = int(input())
A = np.array(input().split(), dtype=np.int32)

left_idx = np.arange(N)
# 自身が左以下ならば0に
left_idx[1:][A[:-1] >= A[1:]] = 0
np.maximum.accumulate(left_idx, out=left_idx)

answer = (np.arange(N) - left_idx).max()
print(answer)

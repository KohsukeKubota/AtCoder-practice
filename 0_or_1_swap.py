import numpy as np


N = int(input())
P = np.array(input().split(), dtype=np.int32)
# sortをそもそもかけずにrange(N)で作成してそれと比較で十分
P_sort = np.sort(P)
diff_P = P != P_sort
diff_num = np.count_nonzero(diff_P)

if diff_num == 0:
    print('YES')
elif diff_num == 2:
    print('YES')
else:
    print('NO')

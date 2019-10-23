import numpy as np


N, L = map(int, input().split())
tasty_list = np.array([L+i-1 for i in range(1, N+1)])
eat_apple_idx = np.argmin(np.abs(tasty_list))
print(np.sum(tasty_list) - tasty_list[eat_apple_idx])


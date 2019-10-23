import math
N = int(input())
R = [int(input()) for _ in range(N)]
R.sort()
if len(R) % 2 == 1:
    sum_ = sum([R[i]**2 if i%2==0 else -R[i]**2 for i in range(len(R))])
else:
    sum_ = sum([R[i]**2 if i%2==1 else -R[i]**2 for i in range(len(R))])
print(sum_ * math.pi)

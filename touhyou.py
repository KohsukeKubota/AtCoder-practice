N = int(input())
S = [input() for _ in range(N)]
dict_ = {}
for s in S:
    if s in dict_: dict_[s] += 1
    else: dict_[s] = 1
print(max(dict_, key=dict_.get))

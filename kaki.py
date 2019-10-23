S = [input() for _ in range(12)]
cnt = 0
for s in S:
    set_ = set(s)
    if 'r' in set_:
        cnt += 1
print(cnt)

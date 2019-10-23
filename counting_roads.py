import collections
N, M = map(int, input().split())
AB = []
for _ in range(M):
    ab = input().split()
    if ab[0] == ab[1]:
        AB.extend([ab[0]])
    else:
        AB.extend(ab)
dic_ = collections.Counter(AB)
list_ = sorted(dic_.items())
for l in list_:
    print(l[1])

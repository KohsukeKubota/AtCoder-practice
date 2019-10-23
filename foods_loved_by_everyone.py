N, M = map(int, input().split())
KA = [list(map(int, input().split())) for _ in range(N)]

all_list = [i for i in range(1, M+1)]
res_set = set()

for i in range(len(KA)):
    diff_set = set(all_list) ^ set(KA[i][1:])
    res_set = res_set | diff_set

print(M - len(res_set))

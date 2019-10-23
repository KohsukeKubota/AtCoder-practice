A = [int(input()) for i in range(5)]
mod_list = [a % 10 for a in A]
mod_list = [10 if a == 0 else a for a in mod_list]

comb_list = [[a, b] for a, b in zip(A, mod_list)]
sort_list = sorted(comb_list, key=lambda x: -x[1])

res = 0

for i, a in enumerate(sort_list):
    if i < 4:
        res += a[0] + (10-a[1])
    else:
        res += a[0]

print(res)

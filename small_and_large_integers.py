A, B, K = map(int, input().split())
if B-A+1 >= 2*K:
    res_list = [i for i in range(A, A+K)] + [i for i in range(B-K+1, B+1)]
else:
    res_list = [i for i in range(A, B+1)]
for i in res_list:
    print(i)

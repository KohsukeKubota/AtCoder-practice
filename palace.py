N = int(input())
T, A = map(int, input().split())
h_list = list(map(int,  input().split()))

temp_diff = 10000
tidx = -1

for i in range(N):
    x = h_list[i]
    temp = T - x*0.006
    abs_temp_diff = abs(A-temp)

    if abs_temp_diff <= temp_diff:
        temp_diff = abs_temp_diff
        tidx = i+1
print(tidx)

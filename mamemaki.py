A = [int(input()) for _ in range(3)]
sorted_idx = sorted(range(len(A)), key=lambda x: -A[x])
for i in range(len(A)):
    print(sorted_idx[i] + 1)

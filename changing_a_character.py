N, K = map(int, input().split())
S = input()

lower_str = S[K-1].lower()

if K == 1:
    print(lower_str + S[K:])
elif 1 < K < N-1:
    print(S[:K-1] + lower_str + S[K:])
elif (K > 1) and (K == N-1):
    print(S[:K-1] + lower_str + S[K])
elif K == N:
    print(S[:K-1] + lower_str)

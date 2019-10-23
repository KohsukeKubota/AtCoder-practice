import heapq
A = list(map(int, input().split()))
A = [-a for a in A]
K = int(input())
heapq.heapify(A)
for i in range(K):
    max_val = heapq.heappop(A)
    heapq.heappush(A, 2*max_val)

print(sum([-a for a in A]))

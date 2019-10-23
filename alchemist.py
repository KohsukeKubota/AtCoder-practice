import heapq
N = int(input())
V = list(map(int, input().split()))
heapq.heapify(V)
while len(V) > 2:
    min_ = heapq.heappop(V)
    second_min = heapq.heappop(V)
    heapq.heappush(V, (min_+second_min)/2)
else: print((V[0] + V[1]) / 2)

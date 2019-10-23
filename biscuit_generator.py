A, B, T = map(int, input().split())
current_time = T + 0.5

q = current_time // A

print(int(B * q))

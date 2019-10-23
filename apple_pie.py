from math import floor


A, P = map(int, input().split())

piece_num = A * 3 + P
print(floor(piece_num/2))

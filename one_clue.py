K, X = map(int, input().split())

start_point = X - K + 1
end_point  = X + K - 1

pos = [i for i in range(start_point, end_point+1)]

print(' '.join(map(str, pos)))

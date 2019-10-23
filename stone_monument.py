a, b = map(int, input().split())
diff_ = b - a
pos1 = sum([i for i in range(1, diff_)])
print(pos1 - a)

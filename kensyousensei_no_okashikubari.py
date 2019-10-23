a, b = int(input()), int(input())
if a == b:
    print(0)
else:
    print(b - (a % b))

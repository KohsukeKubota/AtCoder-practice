A, B, C = map(int, input().split())

accept = A - B
if C - accept > 0:
    print(C-accept)
else:
    print(0)

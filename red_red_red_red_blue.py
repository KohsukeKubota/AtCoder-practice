n, x = map(int, input().split())
to_forward = x-1
to_backward = n-x

if to_forward <= to_backward:
    print(to_forward)
else:
    print(to_backward)

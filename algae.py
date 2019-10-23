r, D, x_int = map(int, input().split())

x = x_int

for i in range(10):
    x_tmp = r*x - D
    print(x_tmp)
    x = x_tmp

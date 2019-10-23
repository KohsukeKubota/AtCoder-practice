N, M, X, Y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

x_list.sort()
y_list.sort()

if x_list[-1] >= y_list[0]:
    print('War')
else:
    z_list = [z for z in range(x_list[-1], y_list[0]+1)]
    z_list.sort()
    if z_list[0] <= X or z_list[-1] > Y:
        print('War')
    else:
        print('No War')

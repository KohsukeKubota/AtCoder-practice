X, Y = input().split()

dict_ = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

if dict_[X] < dict_[Y]:
    print('<')
elif dict_[X] > dict_[Y]:
    print('>')
else:
    print('=')

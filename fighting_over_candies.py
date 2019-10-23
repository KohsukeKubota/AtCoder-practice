abc = list(map(int, input().split()))
abc.sort()
if abc[2] == abc[0]+abc[1]:
    print('Yes')
else:
    print('No')

A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A >= B:
    train_fee = B
else:
    train_fee = A

if C >= D:
    bus_fee = D
else:
    bus_fee = C

print(train_fee + bus_fee)

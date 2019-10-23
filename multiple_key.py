#[アルファベット、数a、数b]
A = [['ABC', 1, 3], ['ZBC', 3, 2], ['DEF', 1, 4]]

print(sorted(A, key=lambda x: x[1]))
print(sorted(A, key=lambda x: (x[1], -x[2])))

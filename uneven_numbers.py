N = int(input())

digits_num = 0
q = 1
n = N

while q > 0:
    q = n // 10
    n = q
    digits_num += 1

one_digits = 9 - 1 + 1 
three_digits = 999 - 100 + 1
five_digits = 99999 - 10000 + 1

if digits_num == 6:
    print(one_digits + three_digits + five_digits)
elif digits_num == 5:
    print(one_digits + three_digits + (N - 10000 + 1))
elif digits_num == 4:
    print(one_digits + three_digits)
elif digits_num == 3:
    print(one_digits + (N - 100 + 1))
elif digits_num == 2:
    print(one_digits)
else:
    print(N - 1 + 1)

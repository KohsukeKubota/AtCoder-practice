n, m = map(int, input().split())
n = n if n < 12 else n - 12
long_ = 0.5 * (n*60+m)
short_ = m * 6
if long_ >= short_:
    res = long_ - short_
else:
    res = short_ - long_
if res <= 180:
    print(res)
else:
    print(360 - res)

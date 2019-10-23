N, X = map(int, input().split())
m_list = [int(input()) for i in range(N)]

mmin = min(m_list)
msum = sum(m_list)
rest_X = X- msum

i = 0

while rest_X >= mmin:
    i += 1
    rest_X -= mmin

print(len(m_list) + i)

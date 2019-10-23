# P:A-B, Q:B-C, R:C-A
P, Q, R = map(int, input().split())

path_list = [P+Q, R+Q, P+R]

print(min(path_list))

s = input()
k = int(input())
list_ = []
idx = 0
while idx+k < len(s):
    target = s[idx:idx+k]
    idx += 1
    if not target in list_:
        list_.append(target)
print(len(set(list_)))

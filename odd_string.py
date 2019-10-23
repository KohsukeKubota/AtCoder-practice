s = input()

tstr = ''
for i in range(len(s)):
    num = i+1
    if num % 2 == 1:
        tstr += s[i]
print(tstr)


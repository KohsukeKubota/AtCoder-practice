S = input()
output = ''
for s in S:
    if s == '0':
        output += '0'
    elif s == '1':
        output += '1'
    else:
        if len(output) != 0:
            output = output[:-1]
print(output)

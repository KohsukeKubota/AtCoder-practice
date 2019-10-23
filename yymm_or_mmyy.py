S = input()

forward = int(S[:2])
backward = int(S[2:])

if (1<=forward<=12) and (1<=backward<=12):
    print('AMBIGUOUS')
elif ((forward == 0) or (12 <= forward <= 99)) and (1<=backward<=12):
    print('YYMM')
elif ((backward == 0) or (12<=backward<=99)) and (1<=forward<=12):
    print('MMYY')
else:
    print('NA')

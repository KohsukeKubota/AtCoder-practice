S = input()
if not S[0].isupper():
    S = S[0].upper() + S[1:]
if not S.islower():
    S = S[0] + S[1:].lower()
print(S)

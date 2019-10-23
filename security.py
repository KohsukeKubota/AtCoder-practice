from sys import exit

S = input()

for i in range(len(S)):
    if i > 0:
        if S[i-1] == S[i]:
            print('Bad')
            exit()

print('Good')

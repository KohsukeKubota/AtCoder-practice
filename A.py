X = input()
alphabet = [chr(i) for i in range(65, 65+5)]

for i in range(len(alphabet)):
    if alphabet[i] == X:
        print(i+1)

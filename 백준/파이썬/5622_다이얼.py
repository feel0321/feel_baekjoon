dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabet = input()
result = 0

for alpha in alphabet:
    for idx in range(8):
        if alpha in dial[idx]:
            result += idx + 3
            break
print(result)
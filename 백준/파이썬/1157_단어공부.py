from collections import Counter

alpha = Counter(input().upper()).most_common(2)
if len(alpha) == 1:
    print(alpha[0][0])
elif alpha[0][1] == alpha[1][1]:
    print('?')
else:
    print(alpha[0][0])
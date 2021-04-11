import sys

num = int(sys.stdin.readline())
count = num

for _ in range(num):
    string = sys.stdin.readline().rstrip()
    alpha = []
    
    for s in string:
        if s not in alpha:
            alpha.append(s)
        elif alpha and s in alpha[:-1]:
           count -= 1
           break
print(count)
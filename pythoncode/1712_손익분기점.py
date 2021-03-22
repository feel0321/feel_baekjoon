a, b, c = map(int, input().split())

dif = c - b
if dif > 0:
    print(a // dif + 1)
else:
    print(-1)
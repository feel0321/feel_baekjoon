s = input()

idx = 97
while idx < 123:
    try:
        print(s.index(chr(idx)), end = ' ')
    except:
        print(-1, end = ' ')
    idx += 1

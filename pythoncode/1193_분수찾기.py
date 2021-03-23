def find(x):
    if x == 1:
        return (1, 1)

    n = 1
    idx = 1
    while x > n:
        idx += 1
        n += idx
    return (idx - (n - x), 1 + (n - x)) if idx % 2 == 0 else (1 + (n - x), idx - (n - x))

x = int(input())
a, b = find(x)
print(str(a) + '/' + str(b))
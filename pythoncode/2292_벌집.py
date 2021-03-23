def howto_bee(n):
    if n == 1:
        return 1
    n -= 1
    idx = 1
    rooms = 6
    while rooms < n:
        idx += 1
        rooms += idx * 6
    return idx + 1

n = int(input())
print(howto_bee(n))
'''
1   => 1개
2 3 4 5 6 7 => 6개
8 9 10 11 12 13 14 15 16 17 18 19 => 12개
20 ~ 37 => 18개
'''
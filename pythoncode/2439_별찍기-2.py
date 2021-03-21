num = int(input())

for n in range(num):
    print(' ' * (num - (n + 1)), end='')
    print('*' * (n + 1))
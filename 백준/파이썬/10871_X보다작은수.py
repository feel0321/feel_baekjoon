import sys

n, x = map(int, sys.stdin.readline().split())
data_list = list(map(int, sys.stdin.readline().split()))

for data in data_list:
    if data < x:
        print(str(data) + ' ', end='')
import sys

command_num, money = map(int, sys.stdin.readline().split())
coin_count = 0
coins = [int(sys.stdin.readline()) for _ in range(command_num)]
coins.sort(reverse=True)
for coin in coins:
    if money >= coin:
        coin_count += money // coin
        money %= coin
print(coin_count)
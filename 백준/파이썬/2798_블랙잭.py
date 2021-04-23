from sys import stdin
from itertools import combinations
input = stdin.readline

count, target = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse = True)
biggest = float('-inf')
for i in combinations(cards, 3):
    temp = sum(i)
    if biggest < temp <= target:
        biggest = temp
print(biggest)
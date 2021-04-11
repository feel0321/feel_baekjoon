import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

for idx in range(10):
    print(str(a * b * c).count(str(idx)))

'''
import sys
from collections import Counter

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
answer = Counter(str(a * b * c))
for idx in range(10):
    print(answer[str(idx)])
'''
import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
print(num2 % 10 * num1)
print(num2 % 100 // 10 * num1)
print(num2 // 100 * num1)
print(num1 * num2)
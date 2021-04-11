import sys

sys.stdin.readline()
num_list = sys.stdin.readline().rstrip()

result = 0
for num in num_list:
    result += int(num)
print(result)
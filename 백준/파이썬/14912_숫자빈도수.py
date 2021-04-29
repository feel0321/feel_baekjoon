# 1 <= n <= 10만, 0 <= d <= 9
n, d = input().split()
answer = 0
for idx in range(int(n)):
    count = str(idx + 1).count(d)
    if count:
        answer += count
print(answer)
def d(n):
    answer = n
    for i in str(n):
        answer += int(i)
    return answer

numbers = []
for idx in range(10000):
    numbers.append(d(idx + 1))
numbers = list(set(numbers))

for idx in range(10000):
    if idx + 1 in numbers:
        pass
    else:
        print(idx + 1)
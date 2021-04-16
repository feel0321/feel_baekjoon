number = int(input())

for num in range(1, number):
    result = 0
    result += num
    num = str(num)
    for n in range(len(num)):
        result += int(num[n])
    if result == number:
        print(num)
        break
#break에 한번도 안걸리면 for else문 처리
else:
    print(0)
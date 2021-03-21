num = input()
first = int(num)
count = 0

while 1:
    if len(num) == 1:#10보다 작다면
        num = '0' + num
    sum = int(num[0]) + int(num[1])
    num = num[-1] + str(sum)[-1]
    count += 1
    if first == int(num):
        break
print(count)
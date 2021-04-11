def hansu(num):
    if num < 100:
        return True
    else:
        num = str(num)
        dif = int(num[0]) - int(num[1])
        count = 1

        for idx in range(1, len(num) - 1):
            dif2 = int(num[idx]) - int(num[idx + 1])
            if dif == dif2:
                count += 1
            if count == len(num) - 1:
                return True
            dif = dif2
        return False

num = int(input())
count = 0

for n in range(1, num + 1):
    if hansu(n):
        count += 1
print(count)
hour, minute = map(int, input().split())

if minute >= 45:
    minute -= 45
else:
    if hour > 0:
        hour -= 1
    else:
        hour = 23
    minute += 15
print(str(hour) + ' ' + str(minute))
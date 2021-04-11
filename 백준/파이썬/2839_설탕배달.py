'''
3kg, 5kg

5kg 봉지만
3kg 봉지만
5+3 섞어서
'''
def check(num):
    bag = 0
    while num > 0:
        if num % 5 == 0:
            bag += 1
            num -= 5
        elif num % 3 == 0:
            bag += 1
            num -= 3
        elif num >= 5:
            bag += 1
            num -= 5
        elif num >= 3:
            bag += 1
            num -= 3
        else:
            return -1
    return bag

num = int(input())
print(check(num))
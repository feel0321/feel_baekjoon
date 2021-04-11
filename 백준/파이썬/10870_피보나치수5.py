def pibonachi(num):
    if num >= 2:
        return pibonachi(num - 1) + pibonachi(num - 2)
    else:
        return num

num = int(input())
print(pibonachi(num))
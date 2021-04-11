'''
1 2 3 4 5 6 7
1 2 4 5 6 7
1 2 4 5 7
1 4 5 7
1 4 5
'''
num, input_idx = map(int, input().split())
men = [idx + 1 for idx in range(num)]
i = input_idx - 1
print('<', end='')
while men:
    print(men.pop(i), end='')
    if not men:
        break
    i += input_idx - 1
    while i > len(men) - 1:
        i -= len(men)
    print(', ', end='')
print('>')

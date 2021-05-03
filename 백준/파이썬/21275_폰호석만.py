import sys

def check(a_dict, b_dict):
    answer = []
    for item in a_dict.items():
        for item2 in b_dict.items():
            if item[0] == item2[0]:
                continue
            if item[1] == item2[1]:
                answer.append((item, item2[0]))
        if len(answer) > 1:
            return answer
    return answer

a, b = sys.stdin.readline().split()
a_dict = dict()
b_dict = dict()

for idx in range(2, 37):
    try:
        a_dict[idx] = int(a, idx)
    except ValueError:
        pass
for idx in range(2, 37):
    try:
        b_dict[idx] = int(b, idx)
    except ValueError:
        pass

answer = check(a_dict, b_dict)
if len(answer) >= 2:
    print('Multiple')
elif len(answer) == 1:
    print(str(answer[0][0][1]) + ' ' + str(answer[0][0][0]) + ' ' + str(answer[0][1]))
else:
    print('Impossible')
'''
0~9
10 a
11 b
...
36 z
'''
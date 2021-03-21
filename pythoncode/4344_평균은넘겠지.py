import sys

case = int(sys.stdin.readline())

for idx in range(case):
    command = list(map(int, sys.stdin.readline().split()))
    student = command[0]
    score = command[1:]
    average = sum(score) / student
    
    over = len([idx for idx in score if idx > average])
    answer = round(float(over / student * 100), 3)
    print(f'{answer:.3f}%')
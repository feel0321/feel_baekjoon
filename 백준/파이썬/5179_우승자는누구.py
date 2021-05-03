from sys import stdin
from collections import defaultdict
input = stdin.readline

case = int(input())
for idx in range(case):
    # 1 <= test <= 10, 1 <= submit <= 5000, 1 <= people <= 500
    test, submit, people = map(int, input().split())
    scores = [0] * people
    solved = [0] * people
    fail = defaultdict(int)
    is_solve = defaultdict(int)

    for _ in range(submit):
        man, test_num, time, is_correct = input().split()
        man = int(man)
        time = int(time)
        is_correct = int(is_correct)

        if is_correct:
            if is_solve[str(man) + test_num]:
                pass
            else:
                scores[man - 1] += time + 20 * fail[str(man) + test_num]
                solved[man - 1] += 1
                is_solve[str(man) + test_num] += 1
        else:
            fail[str(man) + test_num] += 1
    print('Data Set ' + str(idx + 1) + ':')
    # 사람, 푼 문제, 점수
    answer = list(zip(range(1, people + 1), solved, scores))
    # sort key에 -를 붙이면 반대순 (x[1] 내림차순 정렬하고, 같으면 x[2] 오름차순)
    answer.sort(key=lambda x: (-x[1], x[2]))
    for ans in answer:
        print(*ans)
    print()
'''
if 정답 / 오답
정답이면 첫 정답?
정답이면 전까지 오답이 몇번인가? 오답이면 오답 카운트 증가
정답이면 점수 계산 (총점 += 시간 + 20 * 오답 수)
'''
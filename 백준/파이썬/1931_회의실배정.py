'''
Q.회의가 겹치지 않고 최대한 회의를 할 수 있는 개수

회의는 중단 불가
회의가 끝나면 동시에 다음 회의 시작 가능
시작시간과 끝나는 시간이 같으면 시작하자마자 끝난것으로 간주
=> 끝나는 시간에 맞추자
'''
import sys

num = int(sys.stdin.readline())
reservations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num)]
meetings = []
reservations.sort(key = lambda x: (x[1], x[0]))
for reservation in reservations:
    #회의가 없거나, 예약회의 시작시간이 회의종료시간보다 크거나 같으면
    if not meetings or meetings[-1][1] <= reservation[0]:
        meetings.append(reservation)
print(len(meetings))
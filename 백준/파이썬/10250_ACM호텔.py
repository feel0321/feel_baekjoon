import sys

case = int(sys.stdin.readline())

for _ in range(case):
    floor, room, where = map(int, sys.stdin.readline().split())
    hotel = [[0 for r in range(room)] for f in range(floor)]
    
    idx = where % floor
    answer_floor = idx if idx != 0 else idx + floor
    answer_room = (where // floor) + 1 if idx != 0 else where // floor
    print(str(answer_floor) + ('0' + str(answer_room))[-2:] )
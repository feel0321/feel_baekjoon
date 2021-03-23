import sys

def home_people_count(floor, room, home):
    while len(home) <= floor:
        home.append([])
        idx = 1
        while len(home[-1]) < room:
            home[-1].append(sum(home[-2][:idx]))
            idx += 1

case = int(sys.stdin.readline())

for _ in range(case):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    home = [[man + 1 for man in range(room)]]
    print(home)
    home_people_count(floor, room, home)
    print(home)
    print(home[floor][room - 1])
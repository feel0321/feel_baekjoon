import sys

sys.stdin.readline()
times = sys.stdin.readline().split()
times.sort(key = lambda x: int(x))
time_sum = 0
for idx in range(len(times)):
    time_sum += int(times[idx]) * (len(times) - idx)
print(time_sum)
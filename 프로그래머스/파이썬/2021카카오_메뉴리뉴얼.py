import itertools
import collections

def solution(orders, course):
    answer = []
    for c in course:
        log = []
        for order in orders:
            order.sort()
            log += list(itertools.combinations(order, c))
        counter = collections.Counter(log)
        if counter and max(counter.values()) != 1:
            answer += [''.join(c) for c in counter if counter[c] == max(counter.values())]
    answer.sort()
    return answer

# ---- test case 3개
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
#result = ["AC", "ACDE", "BCFG", "CDE"]
print(solution(orders, course))
'''
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
#result = ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(orders, course))

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
#result = ["WX", "XY"]
print(solution(orders, course))
'''
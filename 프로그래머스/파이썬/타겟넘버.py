def solution(numbers, target):
    answer = 0
    
    def check(numbers, target, idx = 0):
        if idx < len(numbers):
            for n_number in [1, -1]:
                numbers[idx] *= n_number
                check(numbers, target, idx + 1)
        elif sum(numbers) == target:
            # 현재있는 check 지역 외에 있는 answer를 사용하겠다는 의미. global은 사용이 권장되지 않음
            nonlocal answer
            answer += 1
            
    check(numbers, target)
    return answer
from collections import Counter

def check():
    # 길이가 짝수
    string = ''
    if len(data) % 2 == 0:
        for item in sorted(counter.items()):
            # 길이가 짝수일 때, 홀수 개수인 알파벳이 있으면 팰린드롬이 안되니까
            if item[1] % 2 == 1:
                print("I'm Sorry Hansoo")
                return
            # 홀수 개수인 알파벳이 없으면 (다 짝수 개수면) string을 절반개수만큼 저장하고, 이후 'string + string뒤집은거' 출력
            string += item[0] * int(item[1] / 2)
        # print('string : ', string)
        print(string + string[::-1])
        return
    # 길이가 홀수
    count = 0
    for item in sorted(counter.items()):
        # 길이가 홀수일 때, 홀수 개수인 알파벳 count
        if item[1] % 2 == 1:
            count += 1
            # 홀수 개수인 알파벳은 한종류여야하니까 2종류면 불가능 처리
            holsu = item[0]
            if count > 1:
                print("I'm Sorry Hansoo")
                return
        # 홀수 개수인 알파벳이 1개면 string을 절반개수만큼 저장하고, 이후 'string + 홀수였던 알파벳 + string뒤집은거' 출력
        string += item[0] * int(item[1] / 2)
    # print('string : ', string)
    print(string + str(holsu) + string[::-1])

data = input()
counter = Counter(data)
check()
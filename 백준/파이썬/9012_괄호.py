import sys

def check(string_command):
    stack = []
    for string in string_command:
        if string == '(':
            stack.append(string)
        else:
            if stack:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if not stack else 'NO'
    
num = int(sys.stdin.readline())
for _ in range(num):
    string_command = sys.stdin.readline().strip()
    print(check(string_command))
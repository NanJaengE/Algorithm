import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    str = input()
    stack = ['']
    TF = 1
    for s in str:
        if s == '{' or s == '(' or s == '[':
            stack.append(s)
        elif s == '}':
            if stack[-1] == '{':    # 1. 괄호가 서로 상쇄
                stack.pop()
            else:                   # 2. 서로 다른 괄호가 올 경우
                TF = 0
                break
        elif s == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                TF = 0
                break
        elif s == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                TF = 0
                break
    if stack != ['']:               # 3. 닫는 괄호만 계속 나왔을 경우
       TF = 0
    print(f'#{test} {TF}')
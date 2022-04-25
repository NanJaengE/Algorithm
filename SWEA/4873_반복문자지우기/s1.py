import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    word = input()
    stack = ['']            # 빈 스택 생성(인덱스 오류 방지를 위해 공백 입력)
    for w in word:
        if stack[-1] == w:  # 스택의 마지막 문자와 같으면
            stack.pop()     # 팝!
        else:
            stack.append(w) # 다르면 넣기
    print(f'#{test} {len(stack)-1}')



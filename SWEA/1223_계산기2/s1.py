import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test in range(1, T+1):
    lens = int(input())
    word = input()
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    # 숫자리스트
    isp = {'+': 1, '*': 2}
    icp = {'+': 1, '*': 2}
    opr_stk = []
    str = ''
    for w in word:                                              # 글자 하나하나 확인
        if w in num:
            str += w
        else:
            while opr_stk and icp[w] <= isp[opr_stk[-1]]:       # 연산자는 딕셔너리를 이용하여 밸류 값 비교하여 들어오는토큰보다 스택토큰이 크다면
                str += opr_stk.pop()                            # 문자열에 연산자 추가
            opr_stk.append(w)
    if opr_stk != []:                                           # for문 종료 후 연산자스택에 연산자가 남았다면
        str += opr_stk.pop()                                    # 추가

    cal_stk = []
    for s in str:
        if s in num:                    # 숫자가 나오면
            cal_stk.append(s)           # 우선 스택에 추가
        else:
            if s == '*':                # 곱하기가 나오면 2개를 꺼내서 곱하고 다시 넣기
                cal_stk.append(int(cal_stk.pop()) * int(cal_stk.pop()))
            elif s == '+':              # 더하기가 나오면 2개를 꺼내서 곱하고 다시 넣기
                cal_stk.append(int(cal_stk.pop()) + int(cal_stk.pop()))

    if len(cal_stk) != 1:               # 만약 마지막 연산자가 곱하기라 원소가 2개이상이라면
        cal_stk.append(int(cal_stk.pop()) + int(cal_stk.pop()))  # 꺼내서 더하고 다시넣기

    print(f'#{test} {cal_stk[0]}')

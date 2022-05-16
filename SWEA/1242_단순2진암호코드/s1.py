import sys
sys.stdin = open('sample_input.txt', 'r')


# 앞 0 잘라내는 함수
def zero_cut_front(str):
    for idx in range(len(str)):
        if str[idx] != '0':
            str = str[idx:len(str)]
            break
    return str


# 뒤 0 잘라내는 함수
def zero_cut_back(str):
    # 뒤 먼저 자르고
    for idx in range(len(str)-1, 0, -1):
        if str[idx] != '0':
            str = str[0:idx+1]
            break
    return str


T = int(input())
for test in range(1, 8):
    N, M = map(int, input().split())
    code = [input().strip() for _ in range(N)]

    # 코드별 대응하는 숫자를 딕셔너리로 저장
    num = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    # 행이 0이 아닐 때 이전에 저장한 행과 다르다면 해당 행을 저장
    line = [0]
    for n in range(N):
        if int(code[n], 16) and line[-1] != code[n]:
            line.append(code[n])
    # 맨 앞 0 삭제
    line.pop(0)

    # 키의 시작이 0이 아니므로 앞 0뭉치 잘라낸 뒤 14의 배수마다 값을 확인하여 0이라면 잘라주기
    for l in range(len(line)):
        line[l] = zero_cut_front(line[l])
        cut = 14

    # 이진수 코드를 담을 리스트
    C = []
    for l in line:
        b = ''
        for i in l:
            b += f'{int(i, base=16):04b}'
        C.append(b)
    # 코드를 해석한 값을 더할 sum 선언
    numsum = 0

    # 코드들을 확인
    for c in C:
        d = ''
        # 코드를 확인하고 뒤쪽 0뭉치 제거할 자를위치 확인
        cutpoint = 0
        for idx in range(len(c) - 1, 0, -1):
            if c[idx] == '1':
                cutpoint = idx + 1
                break
        print(cutpoint)
        if cutpoint < 56:
            # 찾은 컷지점에서 뒤쪽의 0뭉치를 앞으로 넘기기
            move = c[cutpoint:len(c)]
            move += c[0:cutpoint]
            d = move
        elif cutpoint >= 56:
            move = c[cutpoint:len(c)]
            move += c[0:cutpoint]
            for bi in range(len(move)):
                if bi % (cutpoint//56) == 0:
                    d += move[bi]

        print(len(d))
        d = d[len(d)-56:len(d)]

        # 변환한 숫자를 담을 res
        res = []
        for i in range(8):
            res.append(num.get(d[i * 7:(i + 1) * 7]))
        print(res)
        # 인덱스가 홀수일때와 짝수일때를 나누어서 저장
        a = 0
        b = 0
        for i in range(len(res)):
            if i % 2:
                b += res[i]
            else:
                a += res[i]

        # 짝수 인덱스 X 3 + 홀수 인덱스가 10의 배수가 되면 정상코드
        if (a * 3 + b) % 10 == 0:
            numsum += (a + b)

    print(f'#{test} {numsum}')



import sys
sys.stdin = open('input.txt')


def post(v):
    if v:
        post(ch1[v])
        post(ch2[v])
        cal.append(node[v])


def chg_type(char):
    if char.isnumeric():
        return int(char)
    else:
        return char


for test in range(1, 11):
    V = int(input())
    DB = [list(map(chg_type, input().split())) for _ in range(V)]
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    node = [0] * (V + 1)

    for db in DB:
        node[db[0]] = db[1]
        for d in db:
            if db.index(d) == 2:
                ch1[db[0]] = d
            elif db.index(d) == 3:
                ch2[db[0]] = d
    cal = []
    post(1)
    res = []
    for c in cal:
        if type(c) == int:              # 숫자가 나오면
            res.append(c)               # 우선 스택에 추가
        else:
            if c == '*':                # 곱하기가 나오면 2개를 꺼내서 곱하고 다시 넣기
                res.append(res.pop() * res.pop())
            elif c == '+':              # 더하기가 나오면 2개를 꺼내서 곱하고 다시 넣기
                res.append(res.pop() + res.pop())
            elif c == '/':              # 나누기도 똑같이
                x = res.pop()
                y = res.pop()
                res.append(y / x)
            elif c == '-':              # 빼기도 똑같이
                x = res.pop()
                y = res.pop()
                res.append(y - x)

    print(f'#{test} {round(res[0])}')

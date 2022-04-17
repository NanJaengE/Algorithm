import sys
sys.stdin = open('input.txt', 'r')

T = 8
for test in range(1, T+1):
    N = int(input())
    PW = list(map(int, input().split()))

    while PW[-1] > 0:
        for i in range(1, 6):
            res = PW[0]
            PW.pop(0)
            chg = res - i
            if chg > 0:
                PW.append(chg)
            else:
                PW.append(0)
                break
    print(f'#{test} {" ".join(map(str, PW))}')
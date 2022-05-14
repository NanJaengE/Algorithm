import sys
sys.stdin = open('sample_input.txt', 'r')

# 이진수의 부분집합을 구하고 정해진 자릿수에 맞게 가공하고
# 0과 1의 갯수가 반반이 되는 이진수를 경로로 모두 받아옴(ex} N=3, 가로2번/세로2번 = 0011, 0101, ..., 1100)
# 그 뒤 받아온 경로를 다 돌면서 합을 구했으나 N이 충분히 커지니 부분집합을 구하다 시간초과로 문제가 발생함.
# dfs bfs 백트래킹 공부를 다시 해야겠다고 생각하였음.

T = int(input())
for test in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]

    move = []
    for n in range(2**(N-1)-1, 1 << 2*(N-1)):
        B = format(n, 'b').zfill(2*(N-1))
        if B.count('1') == N-1:
            move.append(B)

    mini = 240
    for m in move:
        R = 0
        C = 0
        total = 0
        total += Board[R][C]
        for M in m:
            if M == '1':
                C += 1
                total += Board[R][C]
            else:
                R += 1
                total += Board[R][C]
            if total > mini:
                break
        if total < mini:
            mini = total
    print(f'#{test} {mini}')


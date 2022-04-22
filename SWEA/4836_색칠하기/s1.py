import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N = int(input())
    Board = [[0] * 10 for _ in range(10)]
    for i in range(N):
        Si = list(map(int, input().split()))
        for r in range(Si[0], Si[2]+1):
            for c in range(Si[1], Si[3]+1):
                Board[r][c] += Si[4]

    purple = 0
    for r in range(10):
        for c in range(10):
            if Board[r][c] >= 3:
                purple += 1
    print(f'#{test} {purple}')
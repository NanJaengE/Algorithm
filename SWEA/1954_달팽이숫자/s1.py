import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    dc = [-1, 0, 1, 0]
    dr = [0, 1, 0, -1]
    i = 0
    j = 0
    snail[0][0] = 1
    for num in range(2, N**2+1):
        direction = []
        for k in range(4):
            ni = i + dc[k]
            nj = j + dr[k]
            if 0 <= ni < N and 0 <= nj < N:
                if snail[ni][nj] == 0:
                    direction.append(1)
                else:
                    direction.append(0)
            else:
                direction.append(0)
        if direction == [0, 1, 1, 0] or direction == [0, 1, 0, 0]:
            j += 1
        elif direction == [0, 0, 1, 1] or direction == [0, 0, 1, 0]:
            i += 1
        elif direction == [1, 0, 0, 1] or direction == [0, 0, 0, 1]:
            j -= 1
        elif direction == [1, 1, 0, 0] or direction == [1, 0, 0, 0]:
            i -= 1
        snail[i][j] = num
    print(snail)


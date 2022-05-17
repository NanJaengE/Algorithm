import sys
sys.stdin = open('input.txt', 'r')


def search(r, c):
    check = 0
    path = [[r, c]]
    vis[r][c] = 1

    while True:
        yt, xt = path.pop(0)

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            x = xt + dc[i]
            y = yt + dr[i]

            if 0 <= x < 16 and 0 <= y < 16:
                if Board[y][x] == 0 and vis[y][x] == 0:
                    path.append([y, x])
                    vis[y][x] = 1
                elif Board[y][x] == 3:
                    check = 1
                    break
        if check == 1 or len(path) == 0:
            break

    return check


T = 10
for test in range(1, T+1):
    N = 16
    TT = input()
    Board = [list(map(int, input())) for _ in range(16)]
    vis = [[0]*16 for _ in range(16)]
    r = -1
    c = -1
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 2:
                r = i
                c = j
                break
        if r != -1:
            break

    print(f'#{test} {search(r, c)}')



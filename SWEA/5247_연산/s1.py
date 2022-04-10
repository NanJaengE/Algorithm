import sys
sys.stdin = open('sample_input.txt', 'r')


def bfs(q):
    while q:
        t, cnt = q.pop(0)
        if t == M:
            return cnt
        for i in range(4):
            if i == 0:
                if 1 <= (t + 1) <= 1000000 and visit[t + 1] == 0:
                    q.append([t + 1, cnt + 1])
                    visit[t + 1] = 1
            elif i == 1:
                if 1 <= (t - 1) <= 1000000 and visit[t - 1] == 0:
                    q.append([t - 1, cnt + 1])
                    visit[t - 1] = 1
            # 곱하는애는 무지성으로 자꾸 곱하면 너무 커지기 때문에 추가조건을 달아서 목표숫자보다 작을때만 작동하게
            # 이걸로 시간초과도 해결했습니다
            elif i == 2 and t < M:
                if 1 <= (t * 2) <= 1000000 and visit[t * 2] == 0:
                    q.append([t * 2, cnt + 1])
                    visit[t * 2] = 1
            elif i == 3:
                if 1 <= (t - 10) <= 1000000 and visit[t - 10] == 0:
                    q.append([t - 10, cnt + 1])
                    visit[t - 10] = 1


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    # 두 숫자를 연결하는 가장 빠른 경로를 찾는 문제라고 생각하면 쉽다.
    # 경로는 매 숫자마다 4가지가 존재(-1, +1, *2, -10)경로를 따라 들어갔는데 음수가 되면 안되므로 사전에 걸러주어야 할 것 같다.
    # 최대 100만까지 가능
    visit = [0] * 1000001
    q = []
    q.append([N, 0])
    print(f'#{test} {bfs(q)}')
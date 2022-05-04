import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    Q = [0] * N
    front = 0
    rear = 0
    # 피자 넣기
    for n in range(N):
        Q[n] = pizza[n]
        rear += 1
        if rear == N:
            rear = 0
    # 한바퀴 돈 뒤 먼저 들어간 피자부터 꺼내서 확인 후 치즈가 덜녹았다면 다시넣고, 다녹았다면 다음피자를 그자리에 넣기

    print(f'#{test} {Q}')
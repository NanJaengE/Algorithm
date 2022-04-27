import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    K, N, M = map(int, input().split())              # 값들 받아오기
    stoplist = list(map(int, input().split()))      # 충전 정류소 리스트 받아오기
    print(K, N, M)
    print(stoplist)

    road = [0]*(N+1)
    for stop in stoplist:
        road[stop] = 1

    locate = 0  # 버스 위치 변수 선언
    charge = 0  # 충전횟수를 저장할 변수 선언


    while locate+K <= N:
        for dis in range(K, 0, -1):
            if road[dis]:
                charge += 1
                locate += dis
                break

        else:
            charge = 0
            break

    print(f'#{i} {charge}')
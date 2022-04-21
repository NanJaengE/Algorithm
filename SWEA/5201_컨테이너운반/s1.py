import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 컨테이너와 트럭을 내림차순 정렬(2개뿐이라 함수화안하고 그냥했어용)
    stop = 1
    while stop:
        for n in range(N-1):
            if container[n] < container[n+1]:
                container[n], container[n+1] = container[n+1], container[n]
                break
            if n == N-2:
                stop = 0

    stop = 1
    while stop:
        for m in range(M - 1):
            if truck[m] < truck[m + 1]:
                truck[m], truck[m + 1] = truck[m + 1], truck[m]
                break
            if m == M - 2:
                stop = 0

    total = 0
    n = 0
    # 트럭이나 컨테이너가 존재할 때
    while truck and container:
        M = len(truck)
        # 컨테이너를 꺼내서 비교하고 트럭을 다돌아도 못실으면 버림
        con = container.pop(0)
        for m in range(M):
            # 실을 수 있으면
            if con <= truck[m]:
                total += con
                # 트럭 출발
                truck.pop(m)
                break

    print(f'#{test} {total}')
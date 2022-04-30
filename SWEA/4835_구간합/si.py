import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())        # 숫자카드의 갯수, 합구간의 길이 받기
    num = list(map(int, input().split()))   # 숫자들을 리스트로 받기
    sumlist = []                            # 구간만큼의 sum 값을 저장할 빈 리스트 생성
    for j in range(N-M+1):                  # 반복횟수를 설정하여 앞에서부터 합을 sumlist의 원소로 넣음
        s = 0                               # 원소를 0으로 초기화
        for k in range(M):                  # 123, 234, 345 이렇게 더하도록 인덱스 설정
            s += num[j+k]
        sumlist += [s]                      # sumlist에 누적
    maxi = 0
    mini = sumlist[0]
    for n in sumlist:                       # sumlist에서 최대값 최솟값 찾기
        if maxi < n:
            maxi = n
        if mini >= n:
            mini = n
    print(f'#{T} {maxi-mini}')




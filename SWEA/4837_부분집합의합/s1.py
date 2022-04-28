import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    A = []
    for num in range(1, 13):
        A.append(num)
    count = 0
    for i in range(1 << 12):
        total = 0
        some = []
        for j in range(12):
            if i & (1 << j):
              some.append(A[j])
        if len(some) == N and sum(some) == K:
            count += 1
    print(f'#{test} {count}')
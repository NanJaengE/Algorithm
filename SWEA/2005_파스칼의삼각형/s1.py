import sys
sys.stdin = open('input.txt', 'r')

def Pascal(N, K):
    if N > 0:
        Pascal(N-1, K-1) + Pascal(N-1, K)
    else:
        return 1

T = int(input())
for test in range(1, T+1):
    N = int(input())
    Pascal_list = []
    for i in range(1, N+1):
        Nline = []
        for K in range(i):
            Nline.append(Pascal(N, K))
        Pascal_list.append(Nline)
    print(f'#{test} {" ".join(map(str, Pascal_list))}')


import sys
sys.stdin = open('sample_input.txt', 'r')

def maxi_chg(list, idx, N):         # 최댓값 찾는 함수
    maxidx = idx
    for j in range(idx+1, N):
        if list[maxidx] < list[j]:
            maxidx = j
    list[idx], list[maxidx] = list[maxidx], list[idx]

def mini_chg(list, idx, N):         # 최솟값 찾는 함수
    minidx = idx
    for j in range(idx+1, N):
        if list[minidx] > list[j]:
            minidx = j
    list[idx], list[minidx] = list[minidx], list[idx]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    Number = list(map(int, input().split()))
    for chg in range(N):
        if chg % 2:                 # 인덱스의 나머지가 1이면 최솟값자리
            mini_chg(Number, chg, N)
        else:                       # 0이면 최댓값 자리
            maxi_chg(Number, chg, N)
    print(f'#{test}', end=" ")
    for num in Number:
        print(num, end=" ")
    print()
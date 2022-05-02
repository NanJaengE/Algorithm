import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
print(T)

for i in range(1, T+1):
    times = input()
    num = list(map(int, input().split()))
    mini = num[0]
    maxi = 0
    for j in num:
        if maxi < j:
            maxi = j
        if mini >= j:
            mini = j
    print(f'#{i} {maxi-mini}')




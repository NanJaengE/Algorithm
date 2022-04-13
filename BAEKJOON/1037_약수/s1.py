import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(T):
    N = int(input())
    num = sorted(list(map(int, input().split())))
    if N == 1:
        print(num[0]**2)
    else:
        print(num[0]*num[-1])
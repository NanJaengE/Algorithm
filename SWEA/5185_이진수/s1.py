import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    N, X = input().split()
    B = ''
    for x in X:
        B += f'{int(x, base=16):04b}'
    print(f'#{test} {B}')
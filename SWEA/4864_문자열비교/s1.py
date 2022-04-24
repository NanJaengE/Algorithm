import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test in range(1, 1+T):
    pattern = input()
    word = input()
    print(f'{test} {int(pattern in word)}')

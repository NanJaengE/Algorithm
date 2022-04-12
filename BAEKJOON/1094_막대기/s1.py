import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(T):
    stick = str(format(int(input()), 'b'))
    cnt = 0
    for s in stick:
        if s == '1':
            cnt += 1
    print(cnt)
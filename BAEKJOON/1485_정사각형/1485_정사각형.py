import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(T):
    dot = [list(map(int, input().split())) for _ in range(4)]
    length = []

    length.append((dot[0][0] - dot[1][0]) ** 2 + (dot[0][1] - dot[1][1]) ** 2)
    length.append((dot[0][0] - dot[2][0]) ** 2 + (dot[0][1] - dot[2][1]) ** 2)
    length.append((dot[0][0] - dot[3][0]) ** 2 + (dot[0][1] - dot[3][1]) ** 2)

    length.sort()
    if length[0] == length[1] and length[0] * 2 == length[2]:
        print(1)
    else:
        print(0)
import sys
sys.stdin = open('input.txt', 'r')


def num_make(A, B):
    num = []
    for i in range(1000):
        for j in range(i):
            num.append(i)
            if len(num) >= B:
                return sum(num[A-1:])


T = int(input())
for test in range(T):
    A, B = map(int, input().split())
    print(num_make(A, B))

import sys
sys.stdin = open('input.txt', 'r')


# 소수인지 확인
def check(n):
    if n == 1:
        return False
    for num in range(2, int(n**0.5)+1):
        if n % num == 0:
            return False
    return True


N, M = map(int, input().split())
for i in range(N, M+1):
    if check(i):
        print(i)

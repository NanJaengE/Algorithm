import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, m):



T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    dfs(N, M)

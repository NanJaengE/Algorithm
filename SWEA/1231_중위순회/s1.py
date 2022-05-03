import sys
sys.stdin = open('input.txt', 'r')

def inorder(v):
    if v:
        inorder(ch1[v])
        print(word[v], end='')
        inorder(ch2[v])


for test in range(1, 11):
    V = int(input())
    num = []
    word = [0]*(V+1)
    for j in range(V):
        num.append(list(input().split()))
    for w in num:
        idx = w[0]
        w[0] = int(idx)
        word[w[0]] = w[1]
        w.pop(1)
        for x in w:
            w[w.index(x)] = int(x)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    for n in num:
        for m in n:
            if n.index(m) == 1:
                ch1[n[0]] = m
            elif n.index(m) == 2:
                ch2[n[0]] = m
    print(f'#{test}', end=' ')
    inorder(1)
    print()
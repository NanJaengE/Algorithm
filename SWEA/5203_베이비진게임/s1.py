import sys
sys.stdin = open('sample_input.txt', 'r')


def check(p1, p2):
    # 가진 카드를 정렬 후에 트리플 판단
    play1 = sorted(p1)
    play2 = sorted(p2)
    # 정렬된 카드를 set 으로 중복 제거하여 연속 검사
    splay1 = list(set(play1))
    splay2 = list(set(play2))

    # 1번플레이어 검사
    # 트리플
    for j in range(len(p1)-3):
        if play1[j] == play1[j + 1] == play1[j + 2]:
                return 1
    # 런
    if len(splay1) > 3:
        for s in range(len(splay1)-2):
            if splay1[s] + 2 == splay1[s+1] + 1 == splay1[s+2]:
                return 1

    # 2번플레이어 검사
    # 트리플
    for j in range(len(p2)-3):
        if play2[j] == play2[j + 1] == play2[j + 2]:
                return 2
    # 런
    if len(splay2) > 3:
        for s in range(len(splay2)-2):
            if splay2[s] + 2 == splay2[s+1] + 1 == splay2[s+2]:
                return 2

    # 해당하는게 없으면 0리턴
    return 0


T = int(input())
for test in range(1, T+1):
    drow = list(map(int, input().split()))
    player1 = []
    player2 = []

    for d in range(12):
        if d % 2:
            player2.append(drow[d])
        else:
            player1.append(drow[d])
        # 3장이상 받을때부터는 드로우 할 때 마다 검사
        if d > 5:
            res = check(player1, player2)
            # 승패가 결정나면
            if res:
                print(f'#{test} {res}')
                break
            # 끝까지 가도 승부가 안나면
            elif d == 11 and res == 0:
                print(f'#{test} {res}')

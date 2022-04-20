import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test in range(1, T+1):
    B = input()
    T = input()
    two = len(B) - 1
    three = len(T) - 1
    bi_list = [[] for _ in range(len(B))]
    tri_list = [[[],[]] for _ in range(len(T))]

    # 이진수 경우의 수 확인
    # 이진수의 경우 맨 앞자리는 변화 없으므로 시작을 1로
    for b in range(1, len(B)):
        for bb in range(len(B)):
            if b == bb:
                if B[bb] == '1':
                    bi_list[b].append('0')
                else:
                    bi_list[b].append('1')
            else:
                bi_list[b].append(B[bb])

    # 삼진수 경우의 수 확인
    # 삼진수의 경우 맨 앞자리부터 2개의 경우의 수가 존재.
    for t in range(len(T)):
        for tt in range(len(T)):
            if t == tt:
                if T[tt] == '0':
                    tri_list[t][0].append('1')
                    tri_list[t][1].append('2')
                elif T[tt] == '1':
                    tri_list[t][0].append('0')
                    tri_list[t][1].append('2')
                else:
                    tri_list[t][0].append('0')
                    tri_list[t][1].append('1')
            else:
                tri_list[t][0].append(T[tt])
                tri_list[t][1].append(T[tt])
    # 이진수리스트 맨 앞 빈리스트 제거
    bi_list.pop(0)
    # 만들어진 진수를 join으로 합치고 변환하여 비교할 리스트에 담기
    bi_chg = []
    tri_chg = []
    tri_indexing = []
    for i in bi_list:
        bi_chg.append(int(''.join(i), base=2))
    for i in tri_list:
        tri_chg.append(int(''.join(i[0]), base=3))
        tri_indexing.append(''.join(i[0]))
        tri_chg.append(int(''.join(i[1]), base=3))
        tri_indexing.append(''.join(i[1]))
    bi = int(B, base=2)
    tri = int(T, base=3)

    for b in bi_chg:
        if b in tri_chg:
            ans = b
            break
    print(f'#{test} {ans}')
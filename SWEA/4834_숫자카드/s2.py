import sys
sys.stdin = open("sample_input.txt", "r")

def my_max(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    return num[-1]

def my_count(a,k):
    cnt = 0
    for i in a:
        if i == k:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards =list(map(int,input()))
    result = {} # 카드와 카드장수를 딕셔너리 형식으로 담을것
    # cards를 돌면서 {카드숫자:카드갯수}딕셔너리를 만들어서 result에 저장
    for card in cards:
        result[card]= my_count(cards,card)
    max_card = []   # result의 밸류값 모음

    for i in result:
        max_card.append(result[i])     # 밸류값들을 max_card에 저장

    # if my_count(max_card, my_max(max_card)) == 1: # 가장 많은 카드 장수가 한 장일때
    #     for i in result:
    #         if result[i] == my_max(max_card):   # 맥스와 일치하는 밸류를 가진 키를 찾아 내서
    #             print(f'#{tc} {i} {result[i]}') # 키와 밸류 출력
    # else:                       # 여러 장일 때
    #     ks = []
    #     for i in result:
    #         ks.append(i)        # result의 키 값중 가장 큰 숫자 찾기
    #         mk = my_max(ks)
    #     print(f'#{tc} {mk} {result[mk]}')   # 가장 큰 키를 가진 딕셔너리의 키와 밸류 출력

    alot = []
    for i in result:
        if result[i] == my_max(max_card):
            alot.append(i)
    x = my_max(alot)
    print(f'#{tc} {x} {my_max(max_card)}')
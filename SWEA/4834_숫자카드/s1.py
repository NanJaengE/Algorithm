import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    card = list(map(int, (' '.join(input())).split()))
    card_cnt = {}                       # 카드이름을 key로, 갯수를 value로 할 빈 딕셔너리 생성
    for n in card:                      # 카드 리스트를 돌면서 딕셔너리 value값들을 0으로 초기화
        card_cnt[n] = 0
    for n in card:                      # 초기화된 값들에 카드갯수만큼 +1 누적
        card_cnt[n] += 1
    best = 0                            # 가장 많은 카드를 찾을 기본값 설정
    for most in card_cnt:
        if best < card_cnt.get(most):   # 딕셔너리 값 호출을 이용하여 value값을 비교하고 가장 큰 값 찾기
            best = card_cnt.get(most)
    first = []                          # 가장 많은 카드 갯수를 가진 카드들의 리스트 선언
    for most2 in card_cnt:
        if best == card_cnt.get(most2): # 가장 큰 값을 value값으로 가지는 key값을 리스트에 저장
            first += [most2]

    # 같은 장수의 카드 중 최대값의 카드를 찾기
    maxi = 0
    for j in first:
        if maxi < j:
            maxi = j
    print(f'#{i} {maxi} {card_cnt.get(maxi)}')

import sys
sys.stdin = open('sample_input.txt', 'r')


def bi_search(num_list, num):
    global cnt
    # 없으면 종료
    if num not in num_list:
        return
    # 방향을 담을 스택
    direct = []
    # 초기 인덱스 설정
    start = 0
    end = len(num_list) - 1
    while start <= end:
        middle = (start + end)//2
        if num_list[middle] == num:
            cnt += 1
            return
        elif num_list[middle] > num:
            # 스택 끝값이 반대방향일때 계속 진행
            if direct == [] or direct[-1] == 0:
                end = middle - 1
                direct.append(1)
            else:
                break
        else:
            if direct == [] or direct[-1]:
                start = middle + 1
                direct.append(0)
            else:
                break


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list.sort()
    cnt = 0
    for m in M_list:
        bi_search(N_list, m)
    print(f'#{test} {cnt}')
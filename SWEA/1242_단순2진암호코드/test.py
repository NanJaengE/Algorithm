num = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

# X = '1DB176C588D26EC'
# B = ''
# for x in X:
#     B += f'{int(x, base=16):04b}'
# print(B)

Y = ['3C003FC003C3FC3C3FFFC3FC003C03FC03C003FC3C003C3FC3C3FFFC', 'F83FF07FE0FFFE0FFC1FFFC0007FE0F83FF07FFF07FFF07FE0FFFE0FFC0007C1FF8000', '657A31ABCCB76E',
     '3C3FC3FC3FFC03FC03C3FC3FFC03C03FC3C3FFFC3C3FFFC3C003FC00', '1E01FE1FE001E001FE1E001E1FE1E001FE1FFE1FE1FE1FFE1FFE1FE0']
# 이진수 코드를 담을 리스트
C = []
for y in Y:
    b = ''
    for i in y:
        b += f'{int(i, base=16):04b}'
    C.append(b)
    print(b)
    print(len(b))

# 코드를 해석한 값을 더할 sum 선언
numsum = 0

# 코드들을 확인
for c in C:
    d = ''
    # 코드의 두께에 따라서 다이어트시킨 후 입력
    for bi in range(len(c)):
        if bi % (len(c) // 56) == 0:
            d += c[bi]

    # 코드를 확인하고 뒤쪽 0뭉치 제거할 자를위치 확인
    cutpoint = 0
    for idx in range(len(d) - 1, 0, -1):
        if d[idx] == '1':
            cutpoint = idx + 1
            break

    # 찾은 컷지점에서 뒤쪽의 0뭉치를 앞으로 넘기고 56개만큼 슬라이스하기
    move = d[cutpoint:len(d)]
    move += d[0:cutpoint]
    print(move)
    d = move[len(move) - 56:len(move)]
    print(d)
    # 변환한 숫자를 담을 res
    res = []
    for i in range(8):
        res.append(num.get(d[i * (7):(i + 1) * (7)]))
    # 인덱스가 홀수일때와 짝수일때를 나누어서 저장
    a = 0
    b = 0
    for i in range(len(res)):
        if i % 2:
            b += res[i]
        else:
            a += res[i]

    # 짝수 인덱스 X 3 + 홀수 인덱스가 10의 배수가 되면 정상코드
    if (a * 3 + b) % 10 == 0:
        numsum += (a + b)

print(f'#1 {numsum}')
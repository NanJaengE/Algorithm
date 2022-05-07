import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test in range(T):
    N = input()
    number = []
    for i in N:
        number.append(int(i))
    length = len(number)
    while length > 0:
        length -= 1
        for j in range(length):
            if number[j] < number[j+1]:
                number[j+1], number[j] = number[j], number[j+1]
    print(''.join(map(str, number)))

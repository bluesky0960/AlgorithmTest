#https://www.acmicpc.net/problem/1011

test = int(input())

for i in range(test):
    x, y = map(int, input().split())

    dist = y - x
    cnt = 0
    move = 1
    move_dist = 0
    while move_dist < dist:
        cnt += 1
        move_dist += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)

""" 시간초과
    last = y-1 - (x+1)
    move = 0
    list_a = [0, 1, 2]
    while last != 0:
        for i in list_a[::-1]:
            if last >= i:
                last -= i
                move += 1
                if i == list_a[1]:
                    break
                elif i > list_a[1]:
                    list_a = [x+1 for x in list_a]
                    break
                else:
                    list_a = [x-1 for x in list_a]
                    break

    print(move + 2)
"""
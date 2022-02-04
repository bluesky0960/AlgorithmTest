#https://programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기

def solution(board, moves):
    answer = 0
    size = len(board[0])
    a = []
    for m in moves:
        for i in range(size):
            if board[i][m-1] != 0:
                a.append(board[i][m-1])
                board[i][m-1] = 0
                break
                
        if len(a) == 1 or len(a) == 0:
            continue
        else:
            if a[-1] == a[-2]:
                a.pop()
                a.pop()
                answer+=2
    print(a)
    return answer
#https://www.acmicpc.net/problem/2580
import sys

# 같은 행 숫자 검색
def checkCol(col, num):
    if num in board[col][:]:
        return False
    return True
# 같은 열 숫자 검색
def checkRow(row, num):
    for i in range(9):
        if num == board[i][row]:
            return False
    return True

# 같은 박스 숫자 검색
def checkRect(col, row, num):
    # 박스 시작 위치 설정
    x = col//3 * 3
    y = row//3 * 3
    for i in range(3):
        for j in range(3):
            if board[x+i][y+j] == num:
                return False
    return True

def sudoku(start):
    if start == len(emptyPos):
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        col = emptyPos[start][0]
        row = emptyPos[start][1]

        if checkCol(col, i) and checkRow(row, i) and checkRect(col, row, i):
            board[col][row] = i
            sudoku(start+1)
            board[col][row] = 0

board=[]
# 보드 설정
for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 보드중 0인 곳 찾기
emptyPos = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            emptyPos.append([i,j])

sudoku(0)
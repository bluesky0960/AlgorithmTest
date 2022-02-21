# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기

import sys
from collections import deque

def dfs(x, y):
    isVisited[x][y] = 1
    global cnt
    cnt+=1

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if newX >= 0 and newY >=0 and newX <n and newY <n:
            if isVisited[newX][newY] == 0 and board[newX][newY]=='1':
                dfs(newX, newY)

def bfs(x, y):
    isVisited[x][y] = 1

    global cnt
    cnt += 1

    q = deque()
    q.append((x,y))

    

    while q:
        qx = q[0][0]
        qy = q[0][1]

        q.popleft()

        for i in range(4):
            newX = qx + dx[i]
            newY = qy + dy[i]

            if newX >= 0 and newY >=0 and newX <n and newY <n:
                if isVisited[newX][newY] == 0 and board[newX][newY]=='1':
                    isVisited[newX][newY] = 1
                    q.append((newX, newY))
                    cnt+=1

n = int(sys.stdin.readline())

isVisited = [[0] * (n+1) for _ in range(n+1)]
board = []
house = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
    board.append(sys.stdin.readline())


for i in range(n):
    for j in range(n):
        if isVisited[i][j]==0 and board[i][j]=='1':
            cnt=0
            bfs(i, j)
            house.append(cnt)

house.sort()
print(len(house))
for i in house:
    print(i)

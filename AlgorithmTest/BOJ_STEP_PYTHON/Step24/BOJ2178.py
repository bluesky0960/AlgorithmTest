# https://www.acmicpc.net/problem/2178
# 미로 탐색
from collections import deque
import sys

def bfs():
    isVisited[0][0]=1
    q = deque()

    q.append([0, 0, 1])

    while q:
        qx = q[0][0]
        qy = q[0][1]
        dist = q[0][2]

        q.popleft()

        if qx == n-1 and qy == m-1:
            print(dist)
            return

        for i in range(4):
            newX = qx + dx[i]
            newY = qy + dy[i]

            if newX >=0 and newY >=0 and newX < n and newY < m:
                if isVisited[newX][newY]==0 and board[newX][newY]=='1':
                    isVisited[newX][newY] = 1
                    q.append([newX, newY, dist + 1])

n, m = map(int, sys.stdin.readline().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
board=[]
cnt = 0
isVisited = [[0] * (m+1) for _ in range(n+1)]

for i in range(n):
    board.append(sys.stdin.readline().strip())

bfs()

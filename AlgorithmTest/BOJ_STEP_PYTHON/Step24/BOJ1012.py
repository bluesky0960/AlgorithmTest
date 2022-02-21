#https://www.acmicpc.net/problem/1012
# 유기농 배추
from collections import deque
import sys
# DFS recursion error 해결법
# 1. 백준 재귀 깊이가 1000이기 때문에 아래 코드를 
#    이용해서 깊이를 늘려준다.
# 2. DFS를 BFS로 바꾼다.
sys.setrecursionlimit(10**6)
def dfs(x, y):
    isVisited[x][y] = 1

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if newX >=0 and newY >=0 and newX < n and newY < m:
            if isVisited[newX][newY]==0 and board[newX][newY]==1:
                dfs(newX, newY)

def bfs(x,y):
    isVisited[x][y] = 1
    
    q = deque()

    q.append((x,y))

    while q:
        qx = q[0][0]
        qy = q[0][1]

        q.popleft()

        for i in range(4):
            newX = qx + dx[i]
            newY = qy + dy[i]
            if newX >=0 and newY >=0 and newX < n and newY < m:
                if isVisited[newX][newY]==0 and board[newX][newY]==1:
                    isVisited[newX][newY]=1
                    q.append((newX, newY))




testCase = int(sys.stdin.readline().strip())
dx = [0,1,0,-1]
dy = [-1,0,1,0]
answer = []
for _ in range(testCase):
    m, n, pos = map(int, sys.stdin.readline().split())
    cnt = 0
    board = [[0] * (m) for _ in range(n)]
    isVisited = [[0] * (m) for _ in range(n)]

    for _ in range(pos):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1

    for i in range(n):
        for j in range(m):
            if isVisited[i][j]==0 and board[i][j]==1:
                bfs(i, j)
                cnt+=1
    answer.append(cnt)

for i in answer:
    print(i)
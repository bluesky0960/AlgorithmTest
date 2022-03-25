# https://ktaivle-ai.moducoding.com/Question/1808/View/1
# 달고나

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
isVisited = [[False]*m for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
mat = [sys.stdin.readline().strip() for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if mat[i][j]=='0' and not isVisited[i][j]:
            q = deque()
            q.append((i, j))
            isVisited[i][j] = True
            while q:
                x = q[0][0]
                y = q[0][1]
                q.popleft()

                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m:
                        if mat[new_x][new_y]=='0' and not isVisited[new_x][new_y]:
                            isVisited[new_x][new_y] = True
                            q.append((new_x, new_y))
            cnt+=1
print(cnt)
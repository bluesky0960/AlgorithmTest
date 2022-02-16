# https://www.acmicpc.net/problem/2606
# 바이러스
import sys
from collections import deque

def dfs(start):
    isVisited[start] = 1
    global cnt
    cnt += 1
    for i in range(1, n+1):
        if isVisited[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    isVisited[start] = 1
    
    while q:
        start = q.popleft()
        cnt += 1
        for i in range(1, n+1):
            if isVisited[i] == 0 and graph[start][i]==1:
                q.append(i)
                isVisited[i] = 1
                


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0] * (n+1) for _ in range(n+1)]
isVisited = [0] * (n+1)
cnt = 0
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

# dfs(1)
# print(cnt-1)
bfs(1)
print(cnt-1)
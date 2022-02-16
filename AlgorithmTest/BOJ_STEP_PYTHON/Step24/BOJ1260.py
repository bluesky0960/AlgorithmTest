#https://www.acmicpc.net/problem/1260
# DFS와 BFS
import sys
from collections import deque

def dfs(node):
    # 방문했으므로 1
    isVisited[node] = 1
    print(node, end=' ')
    for i in range(1, n+1):
        # 방문이 안 되었고 mat에 원소가 있다면 재귀
        if isVisited[i] == 0 and mat[node][i] == 1:
            dfs(i)

def bfs(node):
    # q 선언
    q = deque()
    q.append(node)
    
    # 앞써 DFS에서 방문을 한 후 1로 바꿨으니 반대로 0으로 변경
    isVisited[node] = 0
    while q:
        # q앞에서 pop
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, n+1):
            # 방문이 안되고 mat에 원소가 있다면 q에 원소 넣고
            # 방문했다고 변경 후 q에 원소가 없을 때까지 반복
            if isVisited[i] == 1 and mat[node][i] == 1:
                q.append(i)
                isVisited[i] = 0

n, m, v = map(int, sys.stdin.readline().split())
mat = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    mat[x][y] = mat[y][x] = 1

isVisited = [0] * (n+1)

dfs(v)
print()
bfs(v)
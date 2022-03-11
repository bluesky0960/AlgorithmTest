from collections import deque

def solution(n, computers):
    answer = 0
    global isVisited
    isVisited = [0] * n
    for i in range(n):
        if isVisited[i] == 0:
            answer+=1
            isVisited[i] = 1
            def dfs(node):
                isVisited[node] = 1
                for i in range(n):
                    if isVisited[i]==0 and computers[node][i]==1:
                        dfs(i)
            dfs(i)
            # q = deque()
            # q.append(i)
            # while q:
            #     node = q.popleft()
            #     for k in range(n):
            #         if isVisited[k]==0 and computers[node][k]==1:
            #             q.append(k)
            #             isVisited[k] = 1
    return answer
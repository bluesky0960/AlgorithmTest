# https://ktaivle-ai.moducoding.com/Question/1819/View/1
# 홍수 속의 수업

import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        print(q)
        print(distance)
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])
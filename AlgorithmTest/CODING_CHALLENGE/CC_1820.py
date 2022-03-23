# https://ktaivle-ai.moducoding.com/Question/1820/View/1
# 병원

import sys
import heapq

n = int(sys.stdin.readline())
bus = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for _ in range(bus):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
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
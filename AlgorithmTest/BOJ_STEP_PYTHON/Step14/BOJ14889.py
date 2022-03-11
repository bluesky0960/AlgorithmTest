# https://www.acmicpc.net/problem/14889
# 스타트와 링크

from itertools import combinations
import sys

n = int(sys.stdin.readline())
team = n//2
board = []
combi = list(combinations([i for i in range(n)], team))
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split(' '))))

min_score = 1000
for idx, val in enumerate(combi[:len(combi)//2+1]):
    s_score, l_score = 0, 0
    combi_r = len(combi) - idx - 1

    for i in combinations(val, 2):
        s_score += (board[i[0]][i[1]] + board[i[1]][i[0]])

    for j in combinations(combi[combi_r], 2):
        l_score += (board[j[0]][j[1]] + board[j[1]][j[0]])
    if abs(s_score - l_score) < min_score:
        min_score = abs(s_score - l_score)
print(min_score)
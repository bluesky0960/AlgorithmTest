# https://ktaivle-ai.moducoding.com/Question/1831/View/1
# 데이트 자본주의(초급)

import sys

money, n = map(int, sys.stdin.readline().split())
# money = 1000 , 최대 만날 수 있는 사람: 5명
costs = list(map(int, sys.stdin.readline().split()))
# 만날 수 있는 매칭 상대에 드는 비용 list
# 300, 200, 500 ,400, 100
costs.sort(reverse=True)

# 실제 만난 사람
cnt = 0
for i in costs:
    # 1. 1000 - 500 = 500 | n >= 0 
    # 2. 500 - 400 = 100 | n:4 >= 0
    # 3. 100 - 300 = -200 | n:3 >= 0
    # 4. 100 - 200 = -100 | n:3 >=0
    # 5. 100 - 100 = 0 | n:3 >= 0
    if money - i >= 0 and n >=0:
        # 1. money = 500
        # 2. money = 100
        # 5. money = 0
        money -= i
        # 1. cnt = 1
        # 2. cnt = 2
        # 5. cnt = 3
        cnt+=1
        # 1. n = 4
        # 2. n = 3
        # 5. n = 2
        n -= 1

print(cnt)
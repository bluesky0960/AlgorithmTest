# https://ktaivle-ai.moducoding.com/Question/1861/View/1
# 친구야 일어나
import sys
from collections import defaultdict
# 학생 수
n = int(sys.stdin.readline())
# 전화번호부 i 사람이 j명의 전번을 가지고 있음
book = [sys.stdin.readline().strip().split() for _ in range(n)]

# 학생 상태
state = sys.stdin.readline().strip()

stateD = defaultdict(list)
for idx, val in enumerate(state):
    stateD[val].append(idx)
# stateD = {'a':[0,1], 'b':[2]}

# 최소 필요한 학생 수
needs = int(sys.stdin.readline()) - len(stateD['a'])
# 3 - 2 : needs = 1
"""
1. a 전번중 b 통화시간 최솟값
2. 전번이 없으면 연락불가
3. 자던 놈도 깨우면 b->a로 변환 -> 다시 최솟값구하기
4. 사람이 필요한 사람보다 많을 수 있으므로 최솟값중 최솟값을 구해야함

"""
if needs > 0:
    # 여러 b중 깨울때 걸리는 시간
    b_list = []
    for b in stateD['b']: # b = 2
        tmp = [] # [2, 3]
        # a[0,1] -> a[0,1,2]
        for a in stateD['a']: # a = 0, 1
            if a != b:
                tmp.append(int(book[a][b]))
        if len(tmp)==0:
            continue
        tmp.sort() # [2,3]
        b_list.append(tmp[0]) # b_list = [2, 6]
        stateD['a'].append(b) # a[0,1,2]
        print(stateD)
    b_list.sort(reverse=True) # 내림차순 [6, 2]
    cnt = 0
    if len(b_list) >= needs: # 1 >= 1
        for _ in range(needs): # 1
            cnt += b_list.pop() # 최소3명 축제 [2]
        print(cnt)
    else:
        print(-1)
else:
    print(0)
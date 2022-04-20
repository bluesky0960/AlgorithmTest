# https://ktaivle-ai.moducoding.com/Question/1861/View/1
# 친구야 일어나
import sys
import heapq

# 학생 수
n = int(sys.stdin.readline())
# 전화번호부 i 사람이 j명의 전번을 가지고 있음
book = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 학생 상태
state = sys.stdin.readline().strip()
stateCheck = [0]*n

# 최소 필요한 학생 수
needs = int(sys.stdin.readline())

# 예제
# n = 3
# book = 0 1 2
#        1 0 3
#        4 2 0
# state = aab
# needs = 3

q = []

# i = 0, 1, 2
for i in range(n):
    # state[0] = a
    # state[1] = a
    # state[2] = b
    if state[i] == 'a':
        # stateCheck = [1, 1, 0]
        stateCheck[i] = 1
        for j in range(n):
            if i != j:
                heapq.heappush(q, (book[i][j], i, j))

# q = [(book[0][1], 0, 1), (book[0][2], 0, 2), (book[1][0], 1, 0), (book[1][2], 1, 2)]
print(q)
print(stateCheck)
ans = 0
c = False
while q:
    # val = (book[0][1], 0, 1) -> (1, 0, 1)
    # val = (book[0][2], 0, 2) -> (2, 0, 2)
    val = heapq.heappop(q)
    print('val', val)
    # stateCheck = [1, 1, 0]

    # val[2] = 1
    # val[2] = 2
    
    # 첫번째 statecheck[1] = 1 이기 때문에 안됨
    # 두번째 statecheck[2] = 0 이기 때문에 통과
    if stateCheck[val[2]] == 0:
        stateCheck[val[2]] = 1
        # stateCheck = [1,1,1]
        for i in range(n):
            # val[2] = 2
            if i != val[2]:
                # 새로 깨운 애로부터 전화를 걸 수 있게 push
                heapq.heappush(q, (book[val[2]][i], val[2], i))
        # 통화시간 더하기
        ans += val[0]
    # 깨어있는 사람 명수가 최소 필요한 사람과 같으면 break
    if sum(stateCheck) == needs:
        c = True
        break
if c:
    print(ans)
else:
    print(-1)



    
# if needs > 0:
#     # 여러 b중 깨울때 걸리는 시간
#     b_list = []
#     for b in stateD['b']: # b = 2
#         tmp = [] # [2, 3]
#         # a[0,1] -> a[0,1,2]
#         for a in stateD['a']: # a = 0, 1
#             if a != b:
#                 tmp.append(int(book[a][b]))
#         if len(tmp)==0:
#             continue
#         tmp.sort() # [2,3]
#         b_list.append(tmp[0]) # b_list = [2, 6]
#         stateD['a'].append(b) # a[0,1,2]
#         print(stateD)
#     b_list.sort(reverse=True) # 내림차순 [6, 2]
#     cnt = 0
#     if len(b_list) >= needs: # 1 >= 1
#         for _ in range(needs): # 1
#             cnt += b_list.pop() # 최소3명 축제 [2]
#         print(cnt)
#     else:
#         print(-1)
# else:
#     print(0)
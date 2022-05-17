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
# state = aab 3명 중 2명 깨고있고(a) 1명 자고 있다(b)
# needs = 3

q = []

# i = 0, 1, 2
for i in range(n):
    # i=0 -> 1 -> 2
    # state[0] = a
    # state[1] = a
    # state[2] = b
    if state[i] == 'a':
        # stateCheck = [1, 1, 0]
        stateCheck[i] = 1
        # i = 0
        # i = 1
        for j in range(n):
            # j = 0
            # j = 1
            # j = 2
            if i != j:
                heapq.heappush(q, (book[i][j], i, j)) # (1, 0, 1) (2, 0, 2) (1, 1, 0) (3, 1, 2)

# q = [(book[0][1], 0, 1), (book[0][2], 0, 2), (book[1][0], 1, 0), (book[1][2], 1, 2)]

print(q)
# heapq 기본적으로 min heap
# q = (1, 1, 0) (2, 0, 2) (3, 1, 2)
print(stateCheck)
# stateCheck = [1, 1, 0]

ans = 0
c = False

while q:

    val = heapq.heappop(q)
    # 1. val = (1, 0, 1)
    # 2. val = (2, 0, 2)
    print('val', val)
    # stateCheck = [1, 1, 0]

    # val[2] = 1
    # val[2] = 2
    
    # 첫번째 statecheck[1] = 1 이기 때문에 안됨
    # 두번째 statecheck[2] = 0 이기 때문에 통과
    # 1. val = (1, 0, 1)
    # 1. val[2] = 1
    # 1. stateCheck[1] = 1 -> 깨어있음

    # 2. val = (2,0,2)
    # 2. val[2] = 2
    # 2. stateCheck[2] = 0 --> 자고 있음
    if stateCheck[val[2]] == 0:
        stateCheck[val[2]] = 1
        # stateCheck = [1,1,1]

        # 새로 깨어난 사람이 다른 사람을 깨울 때 시간이 최소일때 
        # 깨어있는 사람들 중에 b연락할 때 걸리는 시간이 2, 3
        # 새로 깨운 사람이 b한테 연락을 할때 1
        for i in range(n):
            # val[2] = 2
            # i = 0, val[2] = 2
            if i != val[2]:
                # 새로 깨운 애로부터 전화를 걸 수 있게 push
                heapq.heappush(q, (book[val[2]][i], val[2], i))
                # q = (1, 1, 0) (3, 1, 2) (4, 2, 0) (2, 2, 1)

        # 통화시간 더하기
        # val = (2, 0, 2)
        ans += val[0]
    # 깨어있는 사람 명수가 최소 필요한 사람과 같으면 break
    # statecheck(현재 깨어있는 사람) == needs(축제를 할때 최소 필요한 인원)
    if sum(stateCheck) == needs: # 3==3
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
# https://www.acmicpc.net/problem/5430
# AC
import sys
from collections import deque

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    com = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    q = deque(arr)
    if num==0:
        q=[]
        
    rCnt=0
    isError=False
    for i in com:
        if i == 'R':
            rCnt+=1
        elif i == 'D':
            if len(q) < 1:
                isError=True
                break
            else:
                if rCnt%2 == 0:
                    q.popleft()
                else:
                    q.pop()
    if isError:
        print('error')
    else:
        if rCnt%2==0:
            print('['+','.join(q)+']')
        else:
            q.reverse()
            print('['+','.join(q)+']')
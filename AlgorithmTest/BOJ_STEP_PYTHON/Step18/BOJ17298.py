# https://www.acmicpc.net/problem/17298
# 오큰수
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 다 -1로 채우기
answer = [-1] * n
# 스택에는 arr의 인덱스 번호 저장
stack = [0]

for i in range(1, n):
    # 스택이 안 비어있고 이전 arr숫자보다 현재 arr이
    # 크면 정답 array 인덱스에 넣기
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
"""
answer = []
for i in range(len(arr)):
    tmp = []
    for j in arr[i+1:]:
        if arr[i] < j:
            tmp.append(j)
    tmp.reverse()
    while tmp:
        if tmp[-1] > arr[i]:
            answer.append(tmp.pop())
            break
        else:
            tmp.pop()
    if not tmp and len(answer) != i+1:
        answer.append(-1)
print(*answer)
"""
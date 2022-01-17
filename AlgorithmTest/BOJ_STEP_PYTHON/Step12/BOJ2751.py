# https://www.acmicpc.net/problem/2751
"""
python 라이브러리의 sort는 기본적으로 NlogN의
Time sort사용
-> 그러나 시간 초과 발생
-> 해결방법1: PyPy3을 사용한다
-> 해결방법2: sys 모듈을 이용해서 입력 시간과 
              출력 시간을 줄인다
a.sort()
for i in a:
    print(i)

"""
import sys
a = []
n = int(sys.stdin.readline())
for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
for i in a:
    print(i)

# Max Heap으로 정렬
# import sys
# import heapq
# n = int(sys.stdin.readline())
# h = []
# for _ in range(n):
#     heapq.heappush(h, int(sys.stdin.readline()))

# while h:
#     print(heapq.heappop(h))
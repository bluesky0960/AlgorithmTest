#https://www.acmicpc.net/problem/2750
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
for i in a:
    print(i)

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
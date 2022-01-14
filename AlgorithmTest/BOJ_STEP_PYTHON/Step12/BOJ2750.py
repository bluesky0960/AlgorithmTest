#https://www.acmicpc.net/problem/2750
def mergeSort(n):
    if len(n) <=1:
        print(n)
        return n
    mid = len(n)//2
    left = mergeSort(n[:mid])
    right = mergeSort(n[mid:])
    print(n)
    return n
n = int(input())
a = [int(input()) for _ in range(n)]
mergeSort(a)

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
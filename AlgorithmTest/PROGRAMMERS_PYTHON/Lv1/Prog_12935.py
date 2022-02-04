#https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    min_v = min(arr)
    arr.remove(min_v)
    if len(arr)==0:
        arr.append(-1)
    return arr
    
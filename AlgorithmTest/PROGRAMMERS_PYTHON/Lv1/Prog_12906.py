#https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    answer.append(arr[0])
    count=0
    for i in arr:
        if i != answer[count]:
            answer.append(i)
            count+=1
    return answer
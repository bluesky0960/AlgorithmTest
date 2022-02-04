#https://programmers.co.kr/learn/courses/30/lessons/12953#
def solution(arr):
    answer = 0
    max_n = max(arr)
    while True:
        count = 0
        for i in arr:
            if max_n%i == 0:
                count+=1
            else:
                count = 0
                break
                
        if count == len(arr):
            answer = max_n
            break
        max_n += 1
    
    
    return answer
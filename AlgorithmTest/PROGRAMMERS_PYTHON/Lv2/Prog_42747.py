# https://programmers.co.kr/learn/courses/30/lessons/42747
# H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    start = citations[0]
    while True:
        cnt=0
        for i in citations:
            if start <= i:
                cnt+=1
            else:
                break
        if start <= cnt:
            answer = start
            break
        else:
            start -= 1

    return answer
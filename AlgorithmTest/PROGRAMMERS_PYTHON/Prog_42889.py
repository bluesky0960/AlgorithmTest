#https://programmers.co.kr/learn/courses/30/lessons/42889#

#failure : 클리어못한사람/도달한사람(클리어못한사람+클리어한사람)
#n:전체스테이지수, stages:사용자가 멈춰있는 stages
def solution(N, stages):
    answer = []
    fail = []
    stages.sort()
    
    p = [0] * (N+1)
    for i in stages:
        p[i-1] += 1

    for i in range(len(p)):
        if i < len(p)-1:
            if sum(p[i:]) != 0:
                fail.append((i+1, p[i]/sum(p[i:])))
            else:
                fail.append((i+1, 0))

    fail.sort(key = lambda x:x[1], reverse=True)
    for i in fail:
        answer.append(i[0])
    return answer
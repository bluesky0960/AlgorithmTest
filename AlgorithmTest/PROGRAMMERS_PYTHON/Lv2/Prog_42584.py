# https://programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격

def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt+=1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    return answer
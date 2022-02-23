#https://programmers.co.kr/learn/courses/30/lessons/42583
#다리를 지나는 트럭

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0 for _ in range(bridge_length)])
    t_q = deque(truck_weights)
    days = 0, 0
    while q:
        car = q.popleft()
        weight += car
        if t_q:
            if weight >= t_q[0]:
                t_car = t_q.popleft()
                q.append(t_car)
                weight -= t_car
            if len(q) != bridge_length:
                q.append(0)
            
        days += 1

    answer = days         
        
    return answer
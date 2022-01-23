#https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    
    nicks = {}
    
    for r in record:
        message = r.split()
        if message[0] != 'Leave':
            nicks[message[1]] = message[2]
    
    for r in record:
        message = r.split()
        if message[0] == 'Enter':
            answer.append(f'{nicks[message[1]]}님이 들어왔습니다.')
        elif message[0] == 'Leave':
            answer.append(f'{nicks[message[1]]}님이 나갔습니다.')
            
    return answer
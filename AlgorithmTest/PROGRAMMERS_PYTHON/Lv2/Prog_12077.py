# https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록

def solution(phone_book):
    answer = True
    if len(phone_book)==1:
        return answer
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
                return False
            
    return answer
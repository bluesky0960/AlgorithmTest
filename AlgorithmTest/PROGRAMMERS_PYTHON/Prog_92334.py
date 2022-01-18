# https://programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기
def solution(id_list, report, k):
    report_person = []
    person = {i:0 for i in id_list}
    dic = {}
    report = list(set(report))
    for i in report:
        a, b = i.split()
        if b not in dic.keys():
            dic[b] = 1
        else:
            dic[b] += 1
        if dic[b] == k and b not in report_person:
            report_person.append(b)
    for i in report:
        a, b = i.split()
        if b in report_person:
            person[a] += 1
    answer = list(person.values())
    return answer
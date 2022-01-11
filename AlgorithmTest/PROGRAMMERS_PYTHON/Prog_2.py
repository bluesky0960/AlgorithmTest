#https://programmers.co.kr/learn/courses/30/lessons/72410#
#신규아이디 추천
import re
def solution(new_id):
    answer = ''
    print(new_id)
    
    # Step1
    new_id = new_id.lower()
    print('step1: ', new_id)
    
    # Step2
    pat = re.compile("[a-z0-9-_.]")
    new_id = pat.findall(new_id)
    print('step2: ', new_id)
    # Step3
    count = 0
    for idx, var in enumerate(new_id):
        if var =='.':
            count+=1
            if count == 2:
                new_id[idx-1] = ''
                count = 1
        else:
            count = 0
    new_id = [i for i in new_id if i != '']
    print('step3: ', new_id)

    #Step4
    if len(new_id) != 0:
        if new_id[0] =='.':
            del(new_id[0])
    
        if len(new_id) != 0 and new_id[-1] =='.':
            del(new_id[-1])
    print('step4: ', new_id)
    
    # Step5
    if len(new_id) == 0:
        new_id.append('a')
    print('step5: ', new_id)
    
    # Step6
    if len(new_id) >= 15:
        del(new_id[15:])
    if new_id[-1] =='.':
        del(new_id[-1])
    print('step6: ', new_id)
    
    # Step7
    if len(new_id) < 3:
        while len(new_id) != 3:
            new_id.append(new_id[-1])
    print('step7: ', new_id)
    
    for i in new_id:
        answer += i

    return answer
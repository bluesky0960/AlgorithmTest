# https://programmers.co.kr/learn/courses/30/lessons/81302
# 거리두기 확인하기

def solution(places):
    #맨해튼 거리: (r1, c1) ,(r2, c2) --> |r1-r2| + |c1-c2|
    answer = []
    for i in range(5):
        len_answer = len(answer)
        p_list = []
        
        # 대기실의 모든 참여자(P)찾기)
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    p_list.append([j,k])
        
        # p_list길이가 0이면 참여자가 0이고 1이면 1명밖에 없기 때문에 1 넣기
        if len(p_list) == 0 or len(p_list) == 1:
            answer.append(1)
            continue
        
        m_dist = []
        for p1 in range(len(p_list)):
            dist = 0
            for p2 in range(p1+1, len(p_list)):
                dist = abs(p_list[p1][0] - p_list[p2][0]) + abs(p_list[p1][1] - p_list[p2][1])
                
                # p1, p2 맨해튼 거리가 1이면 붙어있는 것이기 때문에 거리두기x
                if dist == 1:
                    m_dist.clear()
                    answer.append(0)
                    break
                
                # 거리가 2이면 거리두기 검사 진행 
                elif dist == 2:
                    m_dist.append([p_list[p1], p_list[p2]])
                    
                    # 첫번째 좌표 x가 두번째 좌표 x와 같을 때
                    if p_list[p1][0] == p_list[p2][0]:
                        y = (p_list[p1][1] + p_list[p2][1])//2
                        if places[i][p_list[p1][0]][y] == 'O':
                            answer.append(0)
                            break
                    
                    # 첫번째 좌표 y가 두번째 좌표 y와 같을 때
                    elif p_list[p1][1] == p_list[p2][1]:
                        y = (p_list[p1][0] + p_list[p2][0])//2
                        if places[i][y][p_list[p1][1]] == 'O':
                            answer.append(0)
                            break
                    else:
                        # 첫번째 좌표와 두번째 좌표 x,y와 둘 다 다를때
                        up = places[i][p_list[p1][0]][p_list[p2][1]]
                        down = places[i][p_list[p2][0]][p_list[p1][1]]
                        if up == 'O' or down == 'O':
                            answer.append(0)
                            break
            if len_answer != len(answer):
                break
        if len_answer != len(answer):
            continue
        else:
            answer.append(1)
    return answer
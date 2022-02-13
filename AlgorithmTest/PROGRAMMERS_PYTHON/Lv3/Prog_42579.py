#https://programmers.co.kr/learn/courses/30/lessons/42579
#베스트앨범

def solution(genres, plays):
    answer = []
    # 장르: [(고유번호, 플레이횟수), ... , 여러개]
    play_list = {}
    # 장르: 총 플레이횟수
    total_play = {}
    
    cnt = 0
    for g, p in zip(genres, plays):
        if g not in play_list.keys():
            play_list[g] = [(cnt, p)]
            total_play[g] = p
        else:
            play_list[g].append((cnt, p))
            total_play[g] +=p
        cnt+=1
        
    total_play_sorted = sorted(total_play.items(), key=lambda x:x[1], reverse=True)
    
    for g, _ in total_play_sorted:
        # 횟수 내림차순, 번호 오름차순
        play_list[g] = sorted(play_list[g], key=lambda x:(-x[1], x[0]))
        answer.extend([num for num, play in play_list[g][:2]])
    print(play_list)

    return answer
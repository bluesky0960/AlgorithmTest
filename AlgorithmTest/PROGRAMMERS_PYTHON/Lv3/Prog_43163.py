# https://programmers.co.kr/learn/courses/30/lessons/43163
# 단어변환

from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    wordUsed = [False]*len(words)
    q = deque()
    # 시작 단어, 깊이 저장
    q.append([begin, 0])
    while q:
        start, cnt = q.popleft()
        # q에서 뽑은 단어가 target과 같으면 return
        if start == target:
            return cnt
        for i in range(len(words)):
            # 단어 비교후 틀린 철자 수 저장
            tmp = 0
            # 단어비교
            for str1, str2 in zip(start, words[i]):
                if str1 != str2:
                    tmp+=1
            # 한 단어만 틀리고(tmp) 사용안된 단어일때 q에 append
            if tmp==1 and not wordUsed[i]:
                q.append([words[i], cnt+1])
                wordUsed[i] = 1
    return answer
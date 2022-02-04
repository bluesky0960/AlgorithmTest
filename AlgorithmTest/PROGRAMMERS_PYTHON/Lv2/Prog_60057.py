def solution(s):
    if len(s)==1:
        return 1
    
    answer = 1001
    for size in range(1, len(s)//2 + 1):
        t_str = ''
        c_str = ''
        cnt = 0
        for i in range(0, len(s), size):
            if s[i:i+size] != c_str:
                if cnt > 1:
                    t_str += (str(cnt) + c_str)
                else:
                    t_str += c_str
                c_str = s[i:i+size]
                cnt = 1
            else:
                cnt += 1


        if cnt > 1:
            t_str+=(str(cnt) + c_str)
        else:
            t_str+= c_str

        if answer > len(t_str):
            answer = len(t_str)
            
    return answer
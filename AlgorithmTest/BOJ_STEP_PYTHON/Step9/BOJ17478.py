# https://www.acmicpc.net/problem/17478
# 재귀: 재귀함수가 뭔가요?

import sys
def chatbot(n):
    print('____' * (num - n) + s1)
    if n == 0:
        print('____' * (num - n) + s5)
    else:
        print('____' * (num - n) + s2)
        print('____' * (num - n) + s3)
        print('____' * (num - n) + s4)
        tmp = n - 1
        chatbot(tmp)
    print('____' * (num - n) + s6)
    return 0

num = int(sys.stdin.readline().strip())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
s1 = '"재귀함수가 뭔가요?"'
s2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
s3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
s4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
s5 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
s6 = '라고 답변하였지.'
chatbot(num)
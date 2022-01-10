#https://www.acmicpc.net/problem/2675

testCase = int(input())
for i in range(testCase):
    string = ""
    case = input().split()
    for j in case[1]:
        for k in range(int(case[0])):
            string = string + j
    
    print(string)

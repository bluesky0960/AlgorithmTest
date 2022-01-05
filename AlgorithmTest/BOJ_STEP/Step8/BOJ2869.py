#https://www.acmicpc.net/problem/2869

""" 재귀 함수 메모리 폭파
def up(u, d, h, cnt):
    if u >= h:
        return cnt + 1
    else:
        print(h-u+d,":", cnt)
        return up(u, d, h - u + d, cnt+1)
""" 


up_m, down_m, h = map(int, input().split())

print(((h - up_m)//(up_m - down_m) + 1) if (h - up_m) % (up_m - down_m) == 0 else ((h - up_m) // (up_m-down_m)) + 2) 
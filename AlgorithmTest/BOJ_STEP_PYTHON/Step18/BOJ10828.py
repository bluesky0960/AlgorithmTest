#https://www.acmicpc.net/problem/10828
#스택
import sys
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return -1

n = int(sys.stdin.readline().strip())
s = []
for i in range(n):
    code = sys.stdin.readline().strip()
    if code == 'pop':
        if len(s)==0:
            print(-1)
        else:
            print(s.pop())
    if code.startswith('push'):
        _, num = code.split()
        s.append(int(num))
    if code == 'top':
        if len(s)==0:
            print(-1)
        else:
            print(s[-1])
    if code == 'empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
    if code == 'size':
        print(len(s))
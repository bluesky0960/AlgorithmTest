# https://www.acmicpc.net/problem/15552
import sys
testCase = int(sys.stdin.readline().rstrip())

for i in range(testCase):
    a, b = sys.stdin.readline().rstrip().split()
    print(int(a) + int(b))
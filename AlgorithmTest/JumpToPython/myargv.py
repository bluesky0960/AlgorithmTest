import sys

a = list(sys.argv)
del a[0]
sum = 0
for i in a:
    sum += int(i)
print(sum)

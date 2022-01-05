#https://www.acmicpc.net/problem/1193

num = int(input())

line = 0
max_num = 0
while num > max_num:
    line += 1
    max_num += line

gap = max_num - num

if line%2==0:
    top = line - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = line - gap

print(f"{top}/{bottom}")
#num += (4 * (count-1) + 1)
#list_a = [i for i in range(1, (4*(count-1)+2)//2 + 1)]
#print(list_a)
#print(list_a[new_num])

""" 시간초과
list_num_up =   [1, 1, 2]
list_num_down = [1, 2, 1]

count = 2
curCount = 2
down = True

for i in range(3, num):
    print('i: ', i)
    if curCount == count:
        print("cur ", curCount, "count ", count)
        curCount = 1
        count += 1
        if down:
            list_num_up.append(list_num_up[i-1] + 1)
            list_num_down.append(1)
            print("1up: ", list_num_up)
            print("1down: ", list_num_down)
            down = not down
        else:
            list_num_up.append(1)
            list_num_down.append(list_num_down[i-1] + 1)
            print("2up: ", list_num_up)
            print("2down: ", list_num_down)
            down = not down
        print("2.5", down)
    else:
        print("else")
        if down:
            list_num_up.append(list_num_up[i-1] + 1)
            list_num_down.append(list_num_down[i-1] - 1)
            curCount += 1
            print("3up: ", list_num_up)
            print("3down: ", list_num_down)
            print(curCount)
        else:
            list_num_up.append(list_num_up[i-1] - 1)
            list_num_down.append(list_num_down[i-1] + 1)
            curCount += 1
            print("4up: ", list_num_up)
            print("4down: ", list_num_down)
            print(curCount)

"""
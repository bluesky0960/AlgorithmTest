
a, b = input().split()
new_a = '' 
new_b = ''
new_a += a[2]
new_a += a[1]
new_a += a[0]

new_b += b[2]
new_b += b[1]
new_b += b[0]

if int(new_a) > int(new_b):
    print(int(new_a))
else:
    print(int(new_b))

# 거꾸로 뒤집기
# print(a[::-1])
# print("".join(reversed(a)))
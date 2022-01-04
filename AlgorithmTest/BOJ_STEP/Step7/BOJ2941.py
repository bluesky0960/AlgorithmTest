#https://www.acmicpc.net/problem/2941

cAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
st = input()

count = 0

for i in cAlpha:
    st = st.replace(i, '*')
print(len(st))
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
mx_num = 100*1000
vw = [0]*(2*mx_num)
vb = [0]*(2*mx_num)
ans =['']*(2*mx_num)


start = mx_num
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)
    if direction == "L":
        d = -1
        col = "w"
        st = start + d*int(num) + 1
        ed = start
    else:
        d = 1
        col = "b"
        st = start
        ed = start + d*int(num) - 1

    for i in range(st,ed+1):
        if ans[i] == "g":
            continue
        ans[i] = col
        if col == "w":
            vw[i] +=1
        elif col == "b":
            vb[i] +=1
        if vw[i] >= 2 and vb[i] >= 2:
            ans[i] = "g"
    if col == "w":
        start = st
    else:
        start = ed
cnt_w = 0
cnt_b = 0
cnt_g = 0

for i in ans:
    if i == "w":
        cnt_w +=1
    elif i == "b":
        cnt_b +=1
    elif i =="g":
        cnt_g+=1
print(cnt_w,cnt_b,cnt_g)
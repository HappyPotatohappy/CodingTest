import sys
input = sys.stdin.readline

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)
col_list = [[0,0,0] for _ in range(100*1000*2+1)]
now = 100*1000

for xi,di in zip(x,dir):
    if di == "R":
        st = now
        ed = now + xi -1
        now = ed
        col = "b"
        cnt_idx = 1
    else:
        st = now - xi + 1
        ed = now
        now = st
        col = "w"
        cnt_idx = 2
    for i in range(st,ed+1):
        if col_list[i][0] != "g":
            col_list[i][0] = col
            col_list[i][cnt_idx]+=1
            if col_list[i][1] >=2 and col_list[i][2] >=2:
                col_list[i][0]="g"
        
cnt_b = 0
cnt_w = 0
cnt_g = 0
for i in range(100*1000*2+1):
    if col_list[i][0] == "b":
        cnt_b+=1
    elif col_list[i][0] == "w":
        cnt_w+=1
    elif col_list[i][0] == "g":
        cnt_g+=1
sys.stdout.write(str(cnt_w) + " " + str(cnt_b) + " "+ str(cnt_g))
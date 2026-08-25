import sys
input = sys.stdin.readline
offset = 1000
mnum = 2*offset
ax = [[0]*mnum for _ in range(mnum)]
x1,y1,x2,y2 = map(int,input().split())

for i in range(x1,x2):
    for j in range(y1,y2):
        nx = i + offset
        ny = j + offset
        ax[nx][ny] = 1

x1,y1,x2,y2 = map(int,input().split())

for i in range(x1,x2):
    for j in range(y1,y2):
        nx = i + offset
        ny = j + offset
        ax[nx][ny] = 0

x_list = []
y_list = []

for i in range(mnum):
    for j in range(mnum):
        nx = i 
        ny = j 
        if ax[nx][ny] == 1:
            x_list.append(nx)
            y_list.append(ny)
if x_list and y_list:        
    mx = max(x_list)
    my = max(y_list)
    minx = min(x_list)
    miny = min(y_list)
    s = (mx - minx + 1)*(my - miny + 1)
else:
    s = 0
sys.stdout.write(str(s))
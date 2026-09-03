n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0]*n for _ in range(n)]

dxs = [-1,0,1,0]
dys = [0,-1,0,1]

total_cnt = 0

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= n-1

for i in points:
    nowx, nowy = i[0]-1, i[1]-1
    grid[nowx][nowy] = 1
    cnt = 0
    for dx,dy in zip(dxs, dys):
        nx = nowx + dx
        ny = nowy + dy
        if in_range(nx,ny) and grid[nx][ny] == 1:
            cnt +=1
    if cnt == 3:
        print(1)
    else:
        print(0)

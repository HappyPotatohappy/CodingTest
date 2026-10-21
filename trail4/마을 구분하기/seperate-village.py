n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

ans = []

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= n-1

def cango(nx,ny):
    if not in_range(nx,ny):
        return 0
    if grid[nx][ny] == 0:
        return 0
    if visited[nx][ny] == 1:
        return 0
    return 1

def dfs(x,y):
    global cnt

    visited[x][y] = 1
    cnt += 1
    
    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if cango(nx,ny):
            dfs(nx,ny)
    

for i in range(n):
    for j in range(n):
        if cango(i,j):
            cnt = 0
            dfs(i,j)
            ans.append(cnt)
tmp1 = len(ans)
ans.sort()

print(tmp1)

for i in ans:
    print(i)
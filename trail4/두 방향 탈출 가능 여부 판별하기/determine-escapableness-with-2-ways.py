n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dxs = [1, 0]
dys = [0, 1]
def in_range(nx,ny):
    if 0 <= nx <= n-1 and 0 <= ny <= m-1:
        return 1
    else:
        return 0

def can_go(nx,ny):
    if  in_range(nx,ny) and grid[nx][ny]:
        return 1
    else:
        return 0

def dfs(nowx,nowy):
    visited[nowx][nowy] = 1

    for dx, dy in zip(dxs, dys):
        nx = nowx + dx
        ny = nowy + dy
        if can_go(nx,ny) and visited[nx][ny]==0:
            dfs(nx,ny)
    return 

dfs(0,0)
if visited[n-1][m-1]:
    print(1)
else:
    print(0)
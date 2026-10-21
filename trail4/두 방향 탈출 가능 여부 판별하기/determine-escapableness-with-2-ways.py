n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(m)]
is_true = 0

dxs = [1, 0]
dys = [0, 1]

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1

def can_go(nx,ny):
    if not in_range(nx,ny):
        return 0
    if grid[nx][ny] == 0:
        return 0
    if visited[nx][ny] == 1:
        return 0
    return 1


def dfs(x,y):
    global is_true
    if x == n-1 and y == m-1:
        is_true = 1
        return
    
    visited[x][y] = 1

    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny):
            dfs(nx,ny)

dfs(0,0)
print(is_true)
import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1

def cango(nx,ny,k):
    if not in_range(nx,ny):
        return 0
    if visited[nx][ny] == 1:
        return 0
    if grid[nx][ny] <= k:
        return 0
    return 1


def dfs(x,y,k):
    global is_true
    visited[x][y] = 1
    is_true = 1
    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if cango(nx,ny,k):
            dfs(nx,ny,k)


ans = 0
final_k = 0
for k in range(1,101):
    visited = [[0]*m for _ in range(n)]
    tmp = []
    for i in range(n):
        for j in range(m):
            if cango(i,j,k):
                is_true = 0
                dfs(i,j,k)
                tmp.append(is_true)
    if sum(tmp) > ans:
        ans = sum(tmp)
        final_k = k
if ans == 0:
    final_k = 1
print(final_k,ans)
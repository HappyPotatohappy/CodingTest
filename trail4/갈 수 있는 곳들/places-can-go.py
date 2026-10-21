from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

visited = [[0]*n for _ in range(n)]
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= n-1

def cango(nx,ny):
    if not in_range(nx,ny):
        return 0
    if visited[nx][ny]==1:
        return 0
    if grid[nx][ny] == 1:
        return 0
    return 1

q = deque()

def bfs():
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = nowx + dx
            ny = nowy + dy 
            if cango(nx,ny):
                visited[nx][ny] = 1
                q.append([nx,ny])


for x,y in points:
    q.append([x-1,y-1])
    visited[x-1][y-1]=1

bfs()
ans = 0
for i in visited:
    ans += sum(i)
if n == 1:
    ans = 1
print(ans)
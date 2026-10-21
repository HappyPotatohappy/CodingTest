from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
step = [[0]*m for _ in range(n)]
q = deque()
dxs = [0 ,0, 1, -1]
dys = [1, -1, 0, 0]

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1

def cango(nx, ny):
    if not in_range(nx,ny):
        return 0
    if visited[nx][ny] == 1:
        return 0
    if a[nx][ny] == 0:
        return 0
    return 1

def push(nx,ny,s):
    step[nx][ny] = s
    visited[nx][ny] = 1
    q.append([nx,ny])

def bfs():
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = nowx + dx
            ny = nowy + dy
            if cango(nx,ny):
                push(nx,ny,step[nowx][nowy]+1)


push(0,0,0)
bfs()
if step[n-1][m-1] == 0:
    print(-1)
else:
    print(step[n-1][m-1])



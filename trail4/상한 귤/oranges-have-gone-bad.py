from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

q = deque()

step = [[0] *n for _ in range(n)]

visited = [[0]*n for _ in range(n)]
        
def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= n-1

def cango(nx,ny):
    if not in_range(nx,ny):
        return 0
    if visited[nx][ny] == 1:
        return 0
    if grid[nx][ny] == 0:
        return 0
    return 1

def push(nx,ny,s):
    step[nx][ny] = s
    visited[nx][ny] = 1
    q.append([nx,ny])

def bfs():
    while q:
        nowx, nowy = q.popleft()

        for dx,dy in zip(dxs, dys):
            nx = nowx + dx
            ny = nowy + dy
            if cango(nx,ny):
                push(nx,ny,step[nowx][nowy]+1)

cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
           push(i,j,0)
           cnt += 1

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            step[i][j] = -1
        if visited[i][j] == 0 and grid[i][j]==1:
            step[i][j] = -2

for i in step:
    print(*i)
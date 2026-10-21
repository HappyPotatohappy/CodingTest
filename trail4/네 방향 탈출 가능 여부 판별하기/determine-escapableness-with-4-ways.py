from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
dxs = [1,-1,0,0]
dys = [0,0,1,-1]

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1

def cango(nx,ny):
    if not in_range(nx,ny):
        return 0
    if visited[nx][ny] == 1:
        return 0
    if a[nx][ny] == 0:
        return 0
    return 1


def bfs():
    while q:
        nowx,nowy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx = nowx + dx
            ny = nowy + dy
            if cango(nx,ny):
                visited[nx][ny] = 1
                q.append([nx,ny])


q = deque()
q.append([0,0])

bfs()

if visited[n-1][m-1]==1:
    print(1)
else:
    print(0)
        

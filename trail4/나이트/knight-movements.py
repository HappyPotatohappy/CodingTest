from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

r1, c1, r2, c2 = r1 -1, c1 -1, r2 -1, c2 - 1

dxs = [-2, -1, 2, 2, 1, 1, -2, -1]
dys = [-1, -2, -1, 1, -2, 2, 1, 2]
visited = [[0]*n for _ in range(n)]

step = [[-1]*n for _ in range(n)]

q = deque()

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= n-1

def cango(nx,ny):
    if not in_range(nx,ny):
        return 0
    if visited[nx][ny] == 1:
        return 0
    return 1

def push(nx,ny,s):
    step[nx][ny] = s
    visited[nx][ny] = 1
    q.append([nx,ny])

def bfs():
    while q:
        nowx,nowy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = nowx + dx
            ny = nowy + dy
            if cango(nx,ny):
                push(nx,ny,step[nowx][nowy]+1)

push(r1,c1,0)
bfs()

print(step[r2][c2])
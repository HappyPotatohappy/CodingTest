from collections import deque
n,m = map(int,input().split())
grp = []
visited = [[0]*m for _ in range(n)]

q = deque()
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
for i in range(n):
    grp.append(list(map(int,input().split())))

def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1

def can_go(nx,ny):
    return in_range(nx,ny) and grp[nx][ny] and not visited[nx][ny]


def bfs():
    while q:
        nowx,nowy = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx = nowx + dx
            ny = nowy + dy
            if can_go(nx,ny):
                visited[nx][ny] = 1
                q.append([nx,ny])

    



visited[0][0] =1
q.append([0,0])
bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)
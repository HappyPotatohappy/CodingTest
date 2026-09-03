from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
visited = [[0]*m for _ in range(n)]
dxs = [1,-1, 0, 0]
dys = [0, 0, 1, -1]
def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1


def can_go(nx,ny):
    return in_range(nx,ny) and a[nx][ny] and not visited[nx][ny]

def bfs():
    while q:
        nowx,nowy = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx = nowx + dx
            ny = nowy + dy
            if can_go(nx,ny):
                q.append([nx,ny])
                visited[nx][ny] = visited[nowx][nowy] + 1
        
visited[0][0] = 1
q.append([0,0])
bfs()

if not visited[n-1][m-1]:
    print(-1)
else:
    print(visited[n-1][m-1]-1)
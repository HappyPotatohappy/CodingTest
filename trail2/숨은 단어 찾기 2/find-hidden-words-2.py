N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dxs = [1,1,1,-1,-1,-1,0,0]
dys = [0,-1,1,0,-1,1,1,-1]


def in_range(nx,ny):
    return 0 <= nx <= N-1 and 0 <= ny <= M-1

def check(nowx,nowy):
    cnt = 0
    if arr[nowx][nowy] != "L":
        return 0
    else:
        for dx,dy in zip(dxs,dys):
            nx = nowx + dx
            ny = nowy + dy
            if in_range(nx,ny) and arr[nx][ny] == "E":
                nx2 = nx + dx
                ny2 = ny + dy
                if in_range(nx2,ny2) and arr[nx2][ny2] == "E":
                    cnt+=1 
        return cnt

ans = 0
for i in range(N):
    for j in range(M):
        ans += check(i,j)
print(ans)
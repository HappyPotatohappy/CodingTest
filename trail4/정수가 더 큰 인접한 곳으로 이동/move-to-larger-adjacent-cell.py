n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def check_range(nx,ny):
    if 1 <= nx <= n and 1 <= ny <= n:
        return 1
    else:
        return 0

def move(nowx,nowy):
    tmp = []
    for i in range(4):
        nx = nowx + dx[i]
        ny = nowy + dy[i]
        if check_range(nx,ny) and a[nowx][nowy] < a[nx][ny]:
            tmp.append([a[nx][ny],i])
        else:
            tmp.append([101,101])
    tmp.sort(key = lambda x: (x[1]))
    if tmp[0][0]== 101:
        return 0
    else:
        return [nowx+dx[tmp[0][1]], nowy+dy[tmp[0][1]],tmp[0][0]]

ans = [a[r][c]]
while 1:

    new = move(r,c)
    if new == 0:
        break
    ans.append(new[2])
    r = new[0]
    c = new[1]

print(*ans)
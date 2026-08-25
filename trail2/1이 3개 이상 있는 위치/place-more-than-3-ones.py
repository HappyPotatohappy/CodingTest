import sys
input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(nx,ny):
    if nx >=0 and nx < n and ny >=0 and ny < n:
        return 1
    else:
        return 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0
for i in range(n):
    for j in range(n):
        tmp = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if in_range(nx,ny) and grid[nx][ny]:
                tmp += 1
        if tmp >=3:
            cnt += 1
sys.stdout.write(str(cnt))
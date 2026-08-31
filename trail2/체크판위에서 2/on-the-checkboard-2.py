import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
cnt = 0
st_x = 0
sy_y = 0
for i in range(1,R-1):
    for j in range(1,C-1):
        if grid[0][0] != grid[i][j]:
            for k in range(i+1,R-1):
                for l in range(j+1,C-1):
                    if grid[i][j] != grid[k][l] and grid[i][j] == grid[R-1][C-1]:
                        cnt+=1

sys.stdout.write(str(cnt))
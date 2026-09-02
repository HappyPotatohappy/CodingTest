import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 왼쪽 위 사각형을 옮기면서 보자

def get_sc(x,y,grid):
    s = 0
    for i in range(x,x+3):
        for j in range(y,y+3):
            s += grid[i][j]
    return s

if n==3:
    ans = 0
    for i in grid:
        ans += sum(i)
else:
    ans = -sys.maxsize        
    for i in range(n-2):
        for j in range(n-2):
            ans = max(ans,get_sc(i,j,grid))

print(ans)
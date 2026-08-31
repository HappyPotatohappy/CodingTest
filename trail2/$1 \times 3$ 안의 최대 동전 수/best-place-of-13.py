import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

INT_MIN = -sys.maxsize
mxnum = INT_MIN
for i in range(n):
    tmp = 0
    for j in range(n-2):
        tmp = grid[i][j] + grid[i][j+1] + grid[i][j+2]

        if tmp > mxnum:
            mxnum = tmp

sys.stdout.write(str(mxnum))
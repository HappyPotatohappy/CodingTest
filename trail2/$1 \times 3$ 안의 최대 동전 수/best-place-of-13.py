n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
mx = 0
for i in range(n):
    for j in range(n-3+1):
        mx = max(mx,sum(grid[i][j:j+3]))

print(mx)

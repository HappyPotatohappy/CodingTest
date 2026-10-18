n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

mx = 0

for i in range(n-2):
    for j in range(n-2):
        tmp1 = grid[i][j]
        tmp2 = grid[i][j + 1]
        tmp3 = grid[i][j + 2]
        
        tmp4 = grid[i + 1][j]
        tmp5 = grid[i + 2][j]
        
        tmp6 = grid[i + 1][j + 1]
        tmp7 = grid[i + 1][j + 2]
        tmp8 = grid[i + 2][j + 1]
        tmp9 = grid[i + 2][j + 2]

        tm = tmp1 + tmp2 + tmp3 + tmp4 + tmp5 + tmp6 + tmp7 + tmp8 + tmp9
        mx = max(mx,tm)

print(mx)
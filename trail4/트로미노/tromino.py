n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
def in_range(nx,ny):
    return 0 <= nx <= n-1 and 0 <= ny <= m-1
def block1(idx_x,idx_y):
    d1 = 0
    d2 = 1
    d3 = 2
    x1, y1 = idx_x, idx_y
    x2, y2 = x1+1, y1
    x3, y3 = x2, y2+1
    mx = 0
    for i in range(4):
        if in_range(x1,y1) == 0 or in_range(x2,y2) == 0 or in_range(x3,y3) == 0:
            continue
        tmp = grid[x1][y1] + grid[x2][y2] + grid[x3][y3]
        mx = max(mx,tmp)
        x1 = x1 + dxs[d1]
        y1 = y1 + dys[d1]
        
        x2 = x2 + dxs[d2]
        y2 = y2 + dys[d2]

        x3 = x3 + dxs[d3]
        y3 = y3 + dys[d3]

        d1 = (d1 + 1)%4
        d2 = (d2 + 1)%4
        d3 = (d3 + 1)%4
    return mx

def block2(idx_x,idx_y):
    x1, y1 = idx_x, idx_y
    x2, y2 = x1, y1 + 1
    x3, y3 = x1, y1 + 2
    if in_range(x1,y1) and in_range(x2, y2) and in_range(x3, y3):
        tmp1 = grid[x1][y1] + grid[x2][y2] + grid[x3][y3]
    else:
        tmp1 = 0
    

    x4, y4 = x1 + 1, y1
    x5, y5 = x1 + 2, y1
    if in_range(x1,y1) and in_range(x4,y4) and in_range(x5,y5):
        tmp2 = grid[x1][y1] + grid[x4][y4] + grid[x5][y5]
    else:
        tmp2 = 0
    

    mx = max(tmp1, tmp2)
    return mx
    
mx = 0
for i in range(n):
    for j in range(m):
        tmp1 = block1(i,j)
        tmp2 = block2(i,j)
        tmp3 = max(tmp1,tmp2)
        mx = max(mx,tmp3)
print(mx)


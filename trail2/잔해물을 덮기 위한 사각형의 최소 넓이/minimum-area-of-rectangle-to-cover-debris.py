x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
offset = 1000
for i in range(2):
    x1[i] += offset
    x2[i] += offset
    y1[i] += offset
    y2[i] += offset

grid = [[0]*2001 for _ in range(2001)]

for i in range(x1[0],x2[0]):
    for j in range(y1[0],y2[0]):
        grid[i][j] = 1

for i in range(x1[1],x2[1]):
    for j in range(y1[1], y2[1]):
        grid[i][j] = 0

rx = []
ry = []

for i in range(2001):
    for j in range(2001):
        if grid[i][j]:
            rx.append(i)
            ry.append(j)

if not rx:
    print(0)
elif not ry:
    print(o)
else:
    xmx = max(rx) 
    xmn = min(rx) 
    ymx = max(ry) 
    ymn = min(ry) 

    ans = (xmx - xmn + 1) * (ymx - ymn + 1)
    print(ans)
x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

offset = 1000
grid = [[0]*2*offset for _ in range(2*offset)]

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())


for i in range(3):
    x1[i] += offset
    y1[i] += offset
    x2[i] += offset
    y2[i] += offset

for i in range(3):
    if i != 2:
        for j in range(x1[i],x2[i]):
            for k in range(y1[i],y2[i]):
                grid[j][k] = 1
    else:
        for j in range(x1[i],x2[i]):
            for k in range(y1[i],y2[i]):
                grid[j][k] = 0

ans = 0

for i in grid:
    ans += sum(i)

print(ans)
import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

mn = sys.maxsize

for i in range(n):
    xl = []
    yl = []
    for nx,ny in zip(x,y):
        if nx == x[i] and ny == y[i]:
            continue
        xl.append(nx)
        yl.append(ny)
    if xl and yl:
        s = (max(xl) - min(xl)) * (max(yl) - min(yl))
    else:
        s = 0
    mn = min(s,mn)

sys.stdout.write(str(mn))



x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

xm1 = min(x1,a1)
ym1 = min(y1,b1)
xma1 = max(x2,a2)
yma1 = max(y2,b2)

s = (xma1 - xm1) * (yma1 - ym1)
print(s)
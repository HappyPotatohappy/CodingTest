import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
mn = sys.maxsize
for i in range(n):
    mx_x,mn_x,mx_y,mn_y = 0, sys.maxsize,0,sys.maxsize
    for j in range(n):
        if i == j:
            continue
        mx_x = max(mx_x,x[j])
        mn_x = min(mn_x,x[j])
        mx_y = max(mx_y,y[j])
        mn_y = min(mn_y,y[j])
    mn = min((mx_x - mn_x)*(mx_y - mn_y),mn)
print(mn)

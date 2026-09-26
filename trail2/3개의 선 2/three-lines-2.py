import random
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)
visited = [0]*(n)
def check(pt,xys):
    for i in range(3):
        if xys[i] == 0:
            g = pt[i][0]
            for j in range(n):
                if x[j] == g:
                    visited[j]=1
        else:
            g = pt[i][1]
            for j in range(n):
                if y[j] == g:
                    visited[j]=1
    if sum(visited)==n:
        return 1
    else:
        return 0
cand = []
tmp = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            cand.append([i,j,k]) ##  0이면 x축에 평행, 1이면 y축
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if j==k:
                continue
            for xys in cand:
                visited = [0]*n
                p1 = points[i]
                p2 = points[j]
                p3 = points[k]
                pt = [p1,p2,p3]
                tmp += check(pt,xys)
if n <= 3:
    print(1)
else:
    if tmp > 0:
        print(1)
    else:
        print(0)


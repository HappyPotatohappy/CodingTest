import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

def get_dist(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

ans = sys.maxsize
for i in range(1,n-1):
    tmp = 0
    for j in range(n-1):
        if j == i-1:
            tmp += get_dist([x[j],y[j]],[x[j+2],y[j+2]])
            continue
        if j == i:
            continue
        tmp += get_dist([x[j],y[j]],[x[j+1],y[j+1]])
    ans = min(ans,tmp)
print(ans)
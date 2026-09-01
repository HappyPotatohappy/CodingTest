import sys
input = sys.stdin.readline

n,c,g,h = map(int,input().split())

def workcapa(ta,tb,now_t,c,g,h):
    if now_t < ta:
        return c
    elif now_t >= ta and now_t <= tb:
        return g
    else:
        return h
temp = []
for i in range(n):
    ta, tb = map(int,input().split())
    temp.append([ta,tb])
mx = -sys.maxsize
for now_t in range(-10001,10001):
    s = 0
    for ta,tb in temp:
        s += workcapa(ta,tb,now_t,c,g,h)
    mx = max(mx,s)

sys.stdout.write(str(mx))
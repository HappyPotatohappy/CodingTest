import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

tlt = max(sum(t),sum(t_b))

def fill_list(t,d):
    a = [0] * (tlt +1)
    time = 0
    now = 0
    nt = sum(t)
    for ti, di in zip(t,d):
        if di == "R":
            dnum = 1
        else:
            dnum = -1
        for i in range(ti):
            now = now + 1*dnum
            time += 1
            a[time] = now
        now = a[time]
    if nt < tlt:
        for i in range(nt+1,tlt+1):
            a[i] = now    
    return a
    
a = fill_list(t,d)
b = fill_list(t_b,d_b)
cnt = 0
for i in range(1,tlt+1):
    if (a[i-1] > b[i-1] or a[i-1] < b[i-1]) and a[i] == b[i]:
        cnt += 1

sys.stdout.write(str(cnt))
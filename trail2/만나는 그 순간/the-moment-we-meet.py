import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mxnum = 1000*1000
def get_list(d,t):
    a = [(-mxnum*2)]*(mxnum+1)
    now = 0
    time = 0
    for ti,di in zip(t,d):
        if di == "R":
            dnum = 1
        else:
            dnum = -1
        for i in range(ti):
            time +=1
            a[time] = now + (i+1)*dnum
        now = a[time]
    for i in range(time,mxnum+1):
        a[i] = now
    return a
d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))


a = get_list(d,t)
b = get_list(d2,t2)

ans = -1

for i in range(1,mxnum+1):
    if i==0:
        continue
    if a[i] == b[i] and a[i] != (-mxnum*2):
        ans = i
        break

sys.stdout.write(str(ans))


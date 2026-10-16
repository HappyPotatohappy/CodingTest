n, m = map(int, input().split())

mxNum = 2000000
vt_a = [0]*mxNum
vt_b = [0]*mxNum
now_a = 0
now_b = 0
dr = {"L": -1, "R": 1}
a = [0,0]
b = [0,0]
# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)
    di = dr[direction]
    for i in range(now_a+1,now_a+int(time)+1):
        vt_a[i] = vt_a[i-1] + di
    now_a = now_a + int(time)

for j in range(now_a,mxNum):
    vt_a[j] = vt_a[now_a]
# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)
    di = dr[direction]
    for i in range(now_b+1,now_b+int(time)+1):
        vt_b[i] = vt_b[i-1] + di
    now_b = now_b + int(time)
for j in range(now_b,mxNum):
    vt_b[j] = vt_b[now_b]

cnt = 0
for t in range(1,mxNum):
    if (vt_a[t-1] != vt_b[t-1]) and (vt_a[t] == vt_b[t]):
        cnt += 1
    
print(cnt)







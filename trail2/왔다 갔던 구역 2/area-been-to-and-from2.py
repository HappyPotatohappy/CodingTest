n = int(input())
x = []
dir = []
offset = 1000
anslst= [0] * (2*offset)
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

now = offset

for i in range(n):
    lng = x[i]
    d = dir[i]
    if d == "R":
        st = now
        ed = now + lng
        now = ed
    else:
        st = now - lng
        ed = now
        now = st
    
    for j in range(st,ed):
        anslst[j] +=1

cnt = 0
for k in anslst:
    if k >= 2:
        cnt+=1
print(cnt)


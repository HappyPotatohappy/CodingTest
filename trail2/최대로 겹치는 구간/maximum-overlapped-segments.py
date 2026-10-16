n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

vt =[0]*(201)

offset = 100

for st, ed in segments:
    st += offset
    ed += offset
    for i in range(st,ed):
        vt[i] +=1

ans = max(vt)
print(ans)
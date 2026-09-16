N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

def get_stunum(plst):
    plst.sort()
    tp = 0
    cnt = 0
    for i in plst:
        np = tp + i
        if np > B:
            break
        if np < B:
            tp = np
            cnt+=1
        if np == B:
            cnt+=1
            break
    return cnt

tmp_p =[]
mx = 0
for i in range(N):
    tmp_p = P[:]
    tmp_p[i] = tmp_p[i]//2
    mx = max(mx,get_stunum(tmp_p))

print(mx)

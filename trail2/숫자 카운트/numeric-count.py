n = int(input())
a, b, c = [], [], []

def check(i,j,k,num):
    num = list(map(int,str(num)))
    cnt1 = 0
    cnt2 = 0
    cand = [i,j,k]
    for l in range(3):
        for m in range(3):
            if l == m and num[l] == cand[m]:
                cnt1+=1
            if l!=m and num[l] == cand[m]:
                cnt2+=1
    return cnt1,cnt2
                    
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

ans = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or i==k or j==k:
                continue
            cnt = 0
            for s in range(n):
                l = a[s]
                p = b[s]
                q = c[s]
                cnt1, cnt2 = check(i,j,k,l)
                if cnt1 == p and cnt2 == q:
                    cnt+=1
            if cnt == n:
                ans +=1
print(ans)

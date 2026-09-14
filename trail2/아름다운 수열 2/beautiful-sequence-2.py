n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mx = max(B)
blst = [0]*(101)


for i in B:
    blst[i]+=1

def tmplst(numlist):
    tmplst = [0]*(101)
    for i in numlist:
        tmplst[i]+=1
    return tmplst

def check(tplst):
    for i,j in zip(blst,tplst):
        if i!=j:
            return 0
    return 1

ans = 0
if m >n:
    print(ans)
else:
    for i in range(n-m+1):
        st = i
        ed = i + m
        tlst = tmplst(A[st:ed])
        ans += check(tlst)

    print(ans)

                    
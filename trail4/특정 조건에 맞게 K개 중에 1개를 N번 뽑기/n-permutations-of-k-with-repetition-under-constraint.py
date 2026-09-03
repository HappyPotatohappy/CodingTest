k, n = map(int, input().split())
ans= []
def s(loc):
    if loc == n+1:
        print(*ans)
        return
    
    for i in range(1,k+1):
        if loc==1 or loc==2 or ans[-1]!=i or ans[-2]!=i:
            ans.append(i)
            s(loc+1)
            ans.pop()
    return

s(1)
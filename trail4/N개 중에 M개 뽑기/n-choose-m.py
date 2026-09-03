n, m = map(int, input().split())
ans = []
def s(loc,bef):
    if loc == m+1:
        print(*ans)
        return
    
    for i in range(1,n+1):
        if i > bef:
            ans.append(i)
            s(loc+1,i)
            ans.pop()
    return

s(1,0)
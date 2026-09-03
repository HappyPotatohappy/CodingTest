k, n = map(int, input().split())

ans = []

def slect(loc):
    if loc == n+1:
        print(*ans)
        return
    
    for i in range(1,k+1):
        ans.append(i)
        slect(loc+1)
        ans.pop()
    return


slect(1)

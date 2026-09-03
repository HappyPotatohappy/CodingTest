n = int(input())
visited = [0]*(n+1)
ans = []
def s(loc):
    if loc == n+1:
        print(*ans)
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            ans.append(i)
            s(loc+1)
            ans.pop()#
            visited[i] = 0# 이 두줄이 모두 벡트레킹
    return

s(1)

n = int(input())
visited = [0]*(n+1)
arr=[]
def bt(loc):
    if loc == n+1:
        print(*arr)
        return
    
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            bt(loc + 1)
            arr.pop()
            visited[i] = 0

    return

bt(1)
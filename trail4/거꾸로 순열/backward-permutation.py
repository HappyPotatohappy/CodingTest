n = int(input())

arr=[]
visited=[0]*(n+1)

def bt(loc):
    if loc == n+1:
        print(*arr)
        return
    
    for i in range(n,0,-1):
        if visited[i] == 0:
            arr.append(i)
            visited[i]=1
            bt(loc+1)
            arr.pop()
            visited[i]=0
    return
bt(1)

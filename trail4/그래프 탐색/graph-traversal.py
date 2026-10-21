n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
eglst = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for st, ed in edges:
    eglst[st].append(ed)
    eglst[ed].append(st)
cnt = 0
def dfs(vtx):
    global cnt
    for i in eglst[vtx]:
        if not visited[i]:
            visited[i] = 1
            cnt+=1
            dfs(i)
visited[1] = 1
dfs(1)
print(cnt)
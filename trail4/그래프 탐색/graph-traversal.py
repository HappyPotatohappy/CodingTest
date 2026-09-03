n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited = [0]*(1001)
cnt = 0

def bfs(ver):
    global cnt
    for i in li[ver]:
        if visited[i] == 0:
            visited[i] = 1
            cnt+=1
            bfs(i)


li = [[] for _ in range(n+1)]

for i in edges:
    li[i[0]].append(i[1])
    li[i[1]].append(i[0])

visited[1] = 1
bfs(1)
print(cnt)
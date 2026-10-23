import sys
import heapq
INT_MAX = sys.maxsize


n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


lst = [[] for _ in range(n+1)]
relst = [[] for _ in range(n+1)]
for st,ed,w in edges:
    lst[st].append([ed,w])
    relst[ed].append([st,w])

def dijk(x,lst):
    pq = []
    dist = [INT_MAX] *(n+1)
    dist[x] = 0
    heapq.heappush(pq,[0,x])

    while pq:
        min_dist, min_idx = heapq.heappop(pq)

        if dist[min_idx] != min_dist:
            continue
        
        for target_idx, target_dist in lst[min_idx]:
            new_dist = target_dist + min_dist
            if new_dist < dist[target_idx]:
                dist[target_idx] = new_dist
                heapq.heappush(pq,[new_dist,target_idx])
    return dist

dx = dijk(x,lst)
dx2 = dijk(x,relst)
ans = 0
for i in range(1,n+1):
    ans = max(ans,dx[i]+dx2[i])

print(ans)





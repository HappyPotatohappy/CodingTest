import heapq
import sys
INT_MAX = sys.maxsize
n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 가중치가 있는 최단거리니까 다익스트라 가자.
dist = [INT_MAX]*(n+1)
edge_lst = [[] for _ in range(n+1)]
pq = []
for st,ed,w in edges:
    edge_lst[st].append([ed,w])
    edge_lst[ed].append([st,w])

dist[k] = 0
heapq.heappush(pq,[0,k])


while pq:
    min_dist,min_index = heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue
    for target_index, target_dist in edge_lst[min_index]:
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq,[new_dist,target_index])
    

for i in range(1,n+1):
    if dist[i] == INT_MAX:
        dist[i] = -1
    print(dist[i])
        
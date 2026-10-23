import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

pq = []

for i in x:
    if i != 0:
        heapq.heappush(pq,i)
    else:
        if not pq:
            print(0)
        else:
            tmp = heapq.heappop(pq)
            print(tmp)
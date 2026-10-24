N, M = map(int, input().split())

tmp = []
def bt(loc,last):
    if loc == M:
        print(*tmp)
        return
    
    for i in range(1,N+1):
        if i > last:
            tmp.append(i)
            bt(loc+1,i)
            tmp.pop()

 
bt(0,0)
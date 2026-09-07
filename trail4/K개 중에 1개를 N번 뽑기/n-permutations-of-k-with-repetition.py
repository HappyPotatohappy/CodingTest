k, n = map(int, input().split())
arr= [] 
def bt(loc):
    if loc == n+1:
        print(*arr)
        return
    
    for i in range(1,k+1):
        arr.append(i)
        bt(loc + 1)
        arr.pop()
    return 

bt(1)

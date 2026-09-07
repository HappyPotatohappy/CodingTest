n = int(input())

arr= []
cand = []
def bt(loc):
    global cnt
    if loc >= n+1:
        if len(arr)==n:
            cand.append(arr[:])
        return 

    for i in range(1,5):
        for _ in range(i):
            arr.append(i)
        bt(loc+i)
        for _ in range(i):
            arr.pop()
    return
bt(1)

print(len(cand))

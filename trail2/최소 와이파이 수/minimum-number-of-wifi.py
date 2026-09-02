n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

loc = [0]*n

st = 0
ed = 2*m
now = 0
cover = [0]*n
if m == 0:
    print(sum(arr))
else:
    covered_until=-1
    for i in range(n):
        if arr[i] and i > covered_until:
            cnt+=1
            covered_until = i + 2*m


    
    print(cnt)
    


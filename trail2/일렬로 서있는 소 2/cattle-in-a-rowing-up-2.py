n = int(input())
a = list(map(int, input().split()))

a.insert(0,0)
cnt = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            if a[i] <= a[j] and a[j] <= a[k]:
                cnt+=1

print(cnt)

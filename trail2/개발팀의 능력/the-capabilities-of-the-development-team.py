arr = list(map(int, input().split()))
ans = 5000

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    if i==j or i==k or i==l or i==m or j==k or j==l or j==m or k==l or k==l or k==m or l==m:
                        continue
                    gr1 = arr[i] + arr[j]
                    gr2 = arr[k] + arr[l]
                    gr3 = arr[m]
                    if gr1==gr2 or gr2==gr3 or gr1==gr3:
                        continue
                    else:
                        ans = min(ans,max(gr1,gr2,gr3) - min(gr1,gr2,gr3))

if ans != 5000:                                      
    print(ans)
else:
    print(-1)
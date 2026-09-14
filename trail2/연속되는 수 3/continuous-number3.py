n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 1
cnt = 1
for i in range(1,n):
    if arr[i]*arr[i-1] > 0:
        cnt+=1
    else:
        ans = max(ans,cnt)
        cnt = 1
if cnt == n:
    print(n)
else:
    print(ans)
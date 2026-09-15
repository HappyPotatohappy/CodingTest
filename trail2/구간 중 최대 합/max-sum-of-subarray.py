n, k = map(int, input().split())
arr = list(map(int, input().split()))

mx = 0
for i in range(n-k+1):
    mx = max(mx,sum(arr[i:i+k]))

print(mx)


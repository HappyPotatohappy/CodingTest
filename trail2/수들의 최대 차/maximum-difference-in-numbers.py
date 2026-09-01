import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
maxnum = max(arr)
minnum = min(arr)
mx = -sys.maxsize
for i in arr:
    cnt = 0
    for j in range(n):
        if 0 <= arr[j] - i <= k:
            cnt +=1
    mx = max(mx,cnt)

sys.stdout.write(str(mx))
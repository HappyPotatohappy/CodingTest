import sys
input = sys.stdin.readline

mx = -sys.maxsize
n, k = map(int, input().split())
arr = list(map(int, input().split()))



for i in range(n-k+1):
    mx = max(mx,sum(arr[i:i+k]))

sys.stdout.write(str(mx))
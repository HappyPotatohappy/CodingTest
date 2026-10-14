n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0,0)
wifi = [0]*(n+1)
def in_range(nx):
    return 0 <= nx <= n

def check_wifi(idx):#1이 나온 위치를 기준으로 최대한 멀리 와이파이를 설치하고 그 밖 인덱스 반환
    global n,m
    for i in range(idx,n+1):
        if arr[i] == 1:
            if in_range(i+m):
                wifi[i+m] = 1
                if in_range(i + 2*m + 1):
                    return i + 2*m + 1
                else:
                    return 0
            else:
                wifi[n] = 1
                return 0

ans = 0
if m == 0:
    ans = sum(arr)
elif n == 1:
    ans = sum(arr)
elif 2*m > n:
    if sum(arr):
        ans = 1
    else:
        ans = 0
else:
    idx = check_wifi(0)
    while idx:
        idx = check_wifi(idx)
    for k in wifi:
        ans += k
print(ans)

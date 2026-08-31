import sys
input = sys.stdin.readline
def get_avg(lt):
    return (sum(lt)/len(lt))
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i,n):
        avg = get_avg(arr[i:j+1])
        for k in range(i,j+1):
            if arr[k] == avg:
                cnt+=1
                break

sys.stdout.write(str(cnt))

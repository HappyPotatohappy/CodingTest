import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)
def is_pos(max_val,k):
    avail_index = []
    for i,now_val in enumerate(arr):
        if now_val <= max_val:
            avail_index.append(i)
    avail_len = len(avail_index)
    for i in range(1,avail_len):
        dt = avail_index[i] - avail_index[i-1]
        if dt > k:
            return 0
    return 1

minimax = sys.maxsize

for a in range(max_val,max(arr[0],arr[-1])-1,-1):
    if is_pos(a,k):
        minimax = min(minimax,a)

sys.stdout.write(str(minimax))
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

tlt = sum(t)

def fill_list(v,t):
    n = len(t)
    li = [0]*(tlt+1)
    now_idx = 0
    now_loc = 0
    time = 0
    for vi,ti in zip(v,t):
        for i in range(1,ti+1):
            time += 1
            now_loc += vi
            li[time] = now_loc
        
    return li

a = fill_list(v,t)
b = fill_list(v2,t2)

cnt = 0
now_sd = -1 #선두 변수 0이 a 1이 b -1이면 동률

for i in range(1,tlt+1):
    if b[i] > a[i]:
        if now_sd == 0:
            cnt += 1
        now_sd = 1
    elif a[i] > b[i] :
        if now_sd == 1:
            cnt += 1
        now_sd = 0

sys.stdout.write(str(cnt))




# for i in range(1,tlt+1):
#     if (a[i-1]-b[i-1])*(a[i]-b[i]) < 0:
#         cnt +=1
#     elif (a[i] > b[i] or a[i] < b[i]) and (a[i-1]-b[i-1]) == 0:
#         j = 0
#         while 1:
#             if i-1-j ==0:
#                 break
#             if a[i-1-j] != b[i-j-1]:
#                 break
#             j += 1
#         if j == 0:
#             continue
#         else:
#             if (a[i-j-1] - b[i-j-1])*(a[i]-b[i]):
#                 cnt+=1
#sys.stdout.write(str(cnt))
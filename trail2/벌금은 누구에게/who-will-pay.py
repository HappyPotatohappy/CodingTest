import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
stu = [0]*(N+1)
student = [int(input()) for _ in range(M)]
ans = -1
for i in range(M):
    nw = student[i]
    stu[nw] += 1
    if stu[nw] >= K:
        ans = nw
        break

sys.stdout.write(str(ans))

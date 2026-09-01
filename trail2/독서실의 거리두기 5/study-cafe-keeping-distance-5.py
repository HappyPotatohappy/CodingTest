import sys
input = sys.stdin.readline
n = int(input())
seat = input().strip()

seat = list(map(int,list(seat)))
mx = -sys.maxsize
for i in range(n):
    if seat[i]:
        continue
    cop = seat[:]
    cop[i] = 1
    tmp = sys.maxsize
    bef = -1
    for j in range(n):
        if cop[j]:
            if bef == -1:
                bef = j
                continue
            l = j - bef
            bef = j
            tmp = min(tmp,l)

    mx = max(tmp,mx)

sys.stdout.write(str(mx))  
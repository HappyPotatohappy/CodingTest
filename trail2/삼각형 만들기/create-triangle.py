import sys
input = sys.stdin.readline

n = int(input())

pt = []

for i in range(n):
    pt.append(list(map(int,input().split())))

sxmylen = 0 #같은 x 중 가장 길이가 큰 y에 해당하는 그 길이 찾기
symxlen = 0 #같은 y 중 가장 길이가 큰 x에 해당하는 그 길이 찾기
ms = -sys.maxsize
for i in range(n):
    nowx,nowy = pt[i][0], pt[i][1]
    sxmylen = 0 #같은 x 중 가장 길이가 큰 y에 해당하는 그 길이 찾기
    symxlen = 0 #같은 y 중 가장 길이가 큰 x에 해당하는 그 길이 찾기
    for j in range(n):
        if i == j :
            continue
        nx,ny = pt[j][0], pt[j][1]
        if nx == nowx:
            sxmylen = max(sxmylen,abs(ny - nowy))
        if ny == nowy:
            symxlen = max(symxlen,abs(nx - nowx))
    ms = max(symxlen*sxmylen,ms)
sys.stdout.write(str(ms))
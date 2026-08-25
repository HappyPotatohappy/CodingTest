import sys
input = sys.stdin.readline
n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

alToNum = {"W":0,"S":1,"E":2,"N":3}

dx = [-1,0,1,0]
dy = [0,-1,0,1]
nx = 0
ny = 0
for di,dirAl in zip(dist,dir):
    dirnum = alToNum[dirAl]
    nx = nx + dx[dirnum]*di
    ny = ny + dy[dirnum]*di

sys.stdout.write(str(nx)+" "+str(ny))
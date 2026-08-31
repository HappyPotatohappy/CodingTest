import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
s = -sys.maxsize
for i in range(X,Y+1):
    s = max(s,sum(list(map(int,list(str(i))))))

sys.stdout.write(str(s))

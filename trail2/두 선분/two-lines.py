import sys
input = sys.stdin.readline

x1, x2, x3, x4 = map(int, input().split())

if  x3 <= x2 <= x4 or x1 <= x4 <= x2 or (x3 <= x1 and x2 <= x4):
    sys.stdout.write("intersecting")
else:
    sys.stdout.write("nonintersecting")





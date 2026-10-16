x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

xlst = [x1, x2, a1, a2]
ylst = [y1, y2, b1, b2]

xlst.sort()
ylst.sort()

xlen = xlst[-1] - xlst[0]

ylen = ylst[-1] - ylst[0]

print(xlen*ylen)

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

def cover(r1,r2):
    x1, y1, x2, y2 = r1[0], r1[1], r1[2], r1[3]
    a1, b1, a2, b2 = r2[0], r2[1], r2[2], r2[3]

    if x1 <= a1 <= x2 and y1 <= b1 <= y2:
        return 1
    if x1 <= a2 <= x2 and y1 <= b2 <= y2:
        return 1
    if x1 <= a1 <= x2 and y1 <= b2 <= y2:
        return 1
    if x1 <= a2 <= x2 and y1 <= b1 <= y2:
        return 1
    if a1 <= x1 <= a2 and b1 <= y1 <= b2:
        return 1
    if a1 <= x2 <= a2 and b1 <= y2 <= b2:
        return 1
    if a1 <= x1 <= a2 and b1 <= y2 <= b2:
        return 1
    if a1 <= x2 <= a2 and b1 <= y1 <= b2:
        return 1 
    if x1 <= a1 <= x2 and b1 <= y1 <= b2:
        return 1 
    if a1 <= x1 <= a2 and y1 <= b1 <= y2:
        return 1 
    return 0

ans = cover([x1,y1,x2,y2],[a1,b1,a2,b2])
if ans:
    print("overlapping")
else:
    print("nonoverlapping")   



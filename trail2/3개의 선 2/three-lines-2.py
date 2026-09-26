n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

def can_cover(remaining,lines_left):
    if not remaining:
        return True
    if lines_left == 0:
        return False
    
    x0,y0 = remaining[0]

    after_vertical = [p for p in remaining if p[0] != x0]
    if can_cover(after_vertical,lines_left - 1):
        return True
    
    after_horizon = [p for p in remaining if p[1] != y0]
    return can_cover(after_horizon,lines_left-1)

ans = can_cover(points,3)
print(1 if ans else 0)
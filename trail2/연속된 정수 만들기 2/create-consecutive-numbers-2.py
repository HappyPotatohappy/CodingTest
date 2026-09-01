import sys
input = sys.stdin.readline

pos = list(map(int, input().split()))

#p1, p2, p3
#이걸 어떻게 옮겨야 하나... 음...
#p1 을 p2 p3 사이에 음 p1 과 p3중 나머지의 절반 위치쯤 옮겻을 때, 그 값이 작아지는걸 기준으로 해보자.

def comp(pos,cnt):
    p1, p2, p3 = pos[0], pos[1], pos[2]
    d1 = p2 - p1
    d2 = p3 - p2
    if d1 == 1 and d2 ==1:
        return [1, 1, 1], cnt
    elif d1 == 2 :
        cnt+=1
        p3 = (p1+p2)//2
        return [p1,p3,p2],cnt
    elif d2 == 2 :
        cnt+=1
        p1 = (p2+p3)//2
        return [p2,p1,p3],cnt
    elif d1 > 2 and d2 == 1:
        p3 = p1 + 2
        cnt+=1
        return [p1,p3,p2],cnt
    elif d2>2 and d1 == 1:
        p1 = p2 + 2
        cnt+=1
        return [p2,p1,p3],cnt
    elif d1>2 and d2>2:
        if d1 > d2:
            p3 = p1+2
            cnt+=1
            return [p1,p3,p2],cnt
        else:
            cnt+=1
            p1 = p2+2
            return [p2,p1,p3],cnt

cnt = 0

while 1:
    pos.sort()
    pos,cnt = comp(pos,cnt)
    p1, p2, p3 = pos[0], pos[1], pos[2]
    if p1==1 and p2 == 1 and p3 ==1:
        break
print(cnt)
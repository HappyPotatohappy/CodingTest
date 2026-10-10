a, b, x, y = map(int, input().split())

# 어떤 경우들을 잘 정리하면 될까?
# 1. a x y b 인 케이스
# 2. x a      y b or b y 인 케이스
# 3. x    a   b   y
# 4. x  a   y    b
# 그러니까 언제 순간 이동 장치를 쓰면 될까?
# 결국에는 abs(a-x) + abs(b-y) or y x 바뀐 경우도 포함해서 abs(b-a) 보다 작으면
# 이동하면 되는거 아니야?

l1 = abs(a - x)
l2 = abs(b - y)
l3 = abs(b - a)

mn = 100
mn = min(mn,l3)
mn = min(mn, l1 + l2)

l1 = abs(a - y)
l2 = abs(b - x)

mn = min(mn, l1 + l2)

print(mn)

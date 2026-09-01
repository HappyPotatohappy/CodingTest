import sys
input = sys.stdin.readline

a, b, x, y = map(int, input().split())


## a -> b 순간이동 없이
## a->x->y->b로 이동(이때 x가 꼭 b 쪽이라는 보장이 없다.) => |a-x| + |b-y|
## a->y->x->b
ans = min(abs(a-b),abs(a-x)+abs(b-y),abs(a-y)+abs(b-x))
sys.stdout.write(str(ans))
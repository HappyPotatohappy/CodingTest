import random
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)
is_ans = False
for i in range(1,101):
    cnt = 0
    for st,ed in zip(x1,x2):
        if st <= i <= ed:
            cnt += 1
    if cnt == n:
        is_ans = True
        break

if is_ans:
    print("Yes")
else:
    print("No")

# print(100)

# for i in range(100):
#     a = random.randint(1,99)
#     b = random.randint(a,100)
#     print(a,b)
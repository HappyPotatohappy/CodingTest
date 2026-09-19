X, Y = map(int, input().split())

cnt = 0
for nums in range(X, Y+1):
    num = {}
    for s in str(nums):
        if s in num.keys():
            num[s] += 1
        else:
            num[s] = 1
    if len(num) == 2 and min(num.values()) == 1:
        cnt += 1
print(cnt)
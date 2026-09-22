m1, d1, m2, d2 = map(int, input().split())

mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon", "Tue","Wed", "Thu", "Fri", "Sat", "Sun"] 

mday = 0
if m1 > m2:
    for i in range(m2,m1):
        mday -= mon[i]
    mday += d2 - d1
else: 
    for i in range(m1,m2):
        mday += mon[i]

    mday += d2 - d1

print(day[mday%7])

### 아 1월 1일 부터 며칠이 지났는지 카운트 하면~ 아아아아
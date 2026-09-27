m1, d1, m2, d2 = map(int, input().split())

eom = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


# m1, d1가 월요일일 때 m2, d2는 무슨 요일
source = d1
for i in range(m1):
    source += eom[i]
target = d2
for i in range(m2):
    target += eom[i]
    
test = target - source

print(day[test%7])
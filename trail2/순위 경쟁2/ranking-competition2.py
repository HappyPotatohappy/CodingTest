n = int(input())
c = []
s = []
ft = 2 # 0이면 A 1 이면 B 2면 공동 1등
a_score = 0
b_score = 0
cnt = 0
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))
    if ci == "A":
        a_score += int(si)
    else:
        b_score += int(si)
    if a_score > b_score and (ft == 1 or ft == -1 or ft == 2):
        cnt += 1
        ft = 0
    elif b_score > a_score and (ft == 0 or ft == -1 or ft == 2):
        cnt += 1
        ft = 1
    elif a_score == b_score and ft !=2:
        cnt +=1
        ft = 2
print(cnt)
N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

## 아픈 모든 사람들이 먹은 치즈 중 시간대를 고려 했을 때 가능한 공통 치즈를 찾아. 
## 그리고 그 공통 치즈중 가장 많은 사람이 먹은 그 치즈를 먹은 사람의 수가 최대
## 필요 약의 갯수
## 만약에 치즈 기록도 없고 공통 기록도 없으면?? 
## 이런 저런 예외 처리를 좀 잘 해야 할듯.
## 한 사람이 같은 치즈를 여러번 먹는 경우를 고려하지 못 했구나...!!! -> visited로 해결
## 하지만 아직 통과하지 못 했다... 뭐지...
pos_ch = [0]*51
for i in range(S):
    pi,ti = sick_p[i], sick_t[i]
    for j in range(D):
        if t[j] < ti and p[j] == pi:
            pos_ch[m[j]] +=1
pc = []
##여기에서 내가 해야될 건 S에 모든 사람이 먹은 치즈냐 이걸 조건으로 걸어야 한다.

# for j in range(S):
#     scp = sick_p[j]
#     for k in range(D):
#         if scp == p[k]:
#             if pos_ch[m[k]] != 0:
#                 pc.append(m[k]) 

for i in range(1,51):
    if pos_ch[i] != 0:
        cnt = 0
        for j in range(S):
            scp = sick_p[j]
            sct = sick_t[j]
            for k in range(D):
                if p[k]==scp and m[k]==i and sct > t[k]:
                    cnt+=1
                    break
        if cnt == S:
            pc.append(i)

mx = 0
for i in pc:
    cnt = 0
    visited = [0]*(N+1)
    for j in range(D):
        if i==m[j] and visited[p[j]]==0:
            cnt+=1
            visited[p[j]] = 1
    mx = max(mx,cnt)
print(mx)
    


N = int(input())
str = input()

#모든 길이에 대해 부분 수열을 다 만들고 그것이 중복으로 나오는지 탐색해보자
for i in range(1,N+1):
    cand = []
    for j in range(N-i+1):
        cand.append(str[j:j+i])
    is_ans = True
    for k in range(len(cand)):
        for l in range(len(cand)):
            if k == l:
                continue
            if cand[k] == cand[l]:
                is_ans = False
                break
    if is_ans == True:
        print(i)
        break

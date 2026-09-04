# n = int(input())
# arr = []
# cand = []

# def print_answer(num_list):
#     for i in num_list:
#         print(i,end="")
#     print()

# def bt(loc):
#     if loc == n+1:
#         print_answer(arr)
#         return 1
    
#     for i in [4,5,6]:
#         arr.append(i)
#         if check(arr) !=0 and bt(loc+1):
#             return 1
#         arr.pop()
#     return 0

# def check(num_list):
#     for k in range(n):
#         if num_list[-k:] == num_list[-2*k:-k]:
#             return 0

# bt(1)
n = int(input())

# Please write your code here.
# 4,5,6으로만 이루어진 수열
# n개로 이루어진 수열 중 사전순 가장 앞선 것

# 같은 숫자 인접 x
# 같은 수열 인접 x

# 숫자 삽입
# 숫자 삽입 + 앞 숫자와 비교(4면 56중 하나, 5면 46중 하나, 6면 45중 하나)
# 수열 비교 = n_list[i+1:].startswith(n_list[:i+1])

nlist = []

def dfs(i, num):

    nlist.append(num)
    # 수열 비교
    is_duplicate = False
    if len(nlist) > 3:
        for j in range(2, len(nlist)//2 + 1):
            target = ''.join(map(str,nlist[i-j+1:i+1]))
            if ''.join(map(str,nlist[:i-j+1])).endswith(target):
                is_duplicate = True        # 중복
                break

    if not is_duplicate and len(nlist) == n:
        return True

    if is_duplicate:
        nlist.pop()
        return False

    next_num_list = list(set([4,5,6]) - set([num]))
    next_num_list.sort()
    for cand in next_num_list:
        if dfs(i+1, cand):
            return True

    nlist.pop() # 두 후보 다 실패했을 때는 - 되돌리기
    return False

dfs(0, 4)
print(''.join(map(str, nlist)))
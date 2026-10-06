import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 정답의 범위
left = max(a)
right = sum(a)

while left < right:
    mid = (left + right) // 2

    # 각 그룹의 합을 mid 이하로 제한했을 때 필요한 그룹 수
    groups = 1
    current_sum = 0

    for x in a:
        if current_sum + x > mid:
            # 현재 그룹에 넣을 수 없으므로 새 그룹 시작
            groups += 1
            current_sum = x
        else:
            current_sum += x

    if groups <= m:
        # 가능한 상한이므로 더 작은 값도 확인
        right = mid
    else:
        # 상한이 너무 작으므로 더 큰 값 확인
        left = mid + 1

print(left)
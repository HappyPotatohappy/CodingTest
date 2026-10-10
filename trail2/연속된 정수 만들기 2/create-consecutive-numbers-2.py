pos = list(map(int, input().split()))

pos.sort()

if pos[1] - 1 == pos[0] and pos[1] + 1 == pos[2]:
    print(0)
elif pos[1] + 2 == pos[2]:
    print(1)
elif pos[1] -2 == pos[0]:
    print(1)
else:
    print(2)
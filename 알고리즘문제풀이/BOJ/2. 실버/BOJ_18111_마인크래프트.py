import sys

N, M, B = map(int, sys.stdin.readline().split())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = N * M * 256 * 2
ans_target = 0
for target in range(257):
    use_block, take_block = 0, 0         # a = 더 높아서 깎는 양, b = 더 낮아서 채워야 되는 양
    for i in range(N):
        for j in range(M):
            if area[i][j] > target:
                take_block += area[i][j] - target
            else:
                use_block += target - area[i][j]

    if take_block + B >= use_block:      # 낮은 애들을 전부 채울 수 있다면
        if 2 * take_block + use_block <= ans:
            ans = 2 * take_block + use_block
            ans_target = target

print(ans, ans_target)
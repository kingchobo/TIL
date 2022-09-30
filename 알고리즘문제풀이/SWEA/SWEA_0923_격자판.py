t = int(input())
for tc in range(1, t+1):
    area = [list(input().split()) for _ in range(4)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    total = []
    cnt = 0
    for i in range(4):
        for j in range(4):
            result = [area[i][j]]
            for a in range(4):
                ax = i + dx[a]
                ay = j + dy[a]
                if 0 <= ax < 4 and 0 <= ay < 4:
                    result += [area[ax][ay]]
                    for b in range(4):
                        bx = ax + dx[b]
                        by = ay + dy[b]
                        if 0 <= bx < 4 and 0 <= by < 4:
                            result += [area[bx][by]]
                            for c in range(4):
                                cx = bx + dx[c]
                                cy = by + dy[c]
                                if 0 <= cx < 4 and 0 <= cy < 4:
                                    result += [area[cx][cy]]
                                    for e in range(4):
                                        ex = cx + dx[e]
                                        ey = cy + dy[e]
                                        if 0 <= ex < 4 and 0 <= ey < 4:
                                            result += [area[ex][ey]]
                                            for f in range(4):
                                                fx = ex + dx[f]
                                                fy = ey + dy[f]
                                                if 0 <= fx < 4 and 0 <= fy < 4:
                                                    result += [area[fx][fy]]
                                                    for g in range(4):
                                                        gx = fx + dx[g]
                                                        gy = fy + dy[g]
                                                        if 0 <= gx < 4 and 0 <= gy < 4:
                                                            result += [area[gx][gy]]
                                                            temp = ''
                                                            for h in result:
                                                                temp += h
                                                            if temp not in total:
                                                                total.append(temp)
                                                                cnt += 1
                                                            result.pop()
                                                    result.pop()
                                            result.pop()
                                    result.pop()
                            result.pop()
                    result.pop()
    print(f'#{tc} {cnt}')
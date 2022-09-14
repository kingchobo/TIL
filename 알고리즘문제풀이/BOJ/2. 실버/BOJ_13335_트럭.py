n, w, L = map(int, input().split())
waiting = list(map(int, input().split()))

on_the_road = [0] * w
arrived = []
time = 0

while len(arrived) != n:
    time += 1
    if on_the_road[0] == 0:
        del on_the_road[0]
    else:
        arrived.append(on_the_road.pop(0))

    if waiting and sum(on_the_road) + waiting[0] <= L:
        on_the_road.append(waiting.pop(0))
    else:
        on_the_road.append(0)

print(time)
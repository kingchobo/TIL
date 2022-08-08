N = int(input())
conf_list = []
for n in range(N):
    conf_list.append(list(map(int, input().split())))
# 받은 자료를 시작시간 기준으로 오름차순 정렬
conf_list.sort(key=lambda x:x[0])
# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]

max = 0
for i in range(N):
    end_time_list = []
    end_time_list.append(conf_list[0][1])
    for time in conf_list[1:]:
        if end_time_list[-1] <= time[0]:
            end_time_list.append(time[1])
    if len(end_time_list) > max:
        max = len(end_time_list)
    del conf_list[0]
print(max)
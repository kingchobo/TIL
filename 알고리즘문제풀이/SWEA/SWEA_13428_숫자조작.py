# 최대값 만들기
def max_num(M_list):
    for _ in range(len(M_list)):
        new_list = M_list[:]
        if max(new_list) != new_list[0]:
            break
        else:
            new_list = M_list[1:]

    for i in new_list[::-1]:
        if i == max(new_list):
            M = new_list.index(i)
            break
    new_list[0], new_list[M] = new_list[M], new_list[0]
    answer = M_list[:len(M_list)-len(new_list)] + new_list
    answer = ''.join(list(map(str, answer)))
    return answer

# 최소값 만들기
def min_num(m_list):
    for i in m_list[::-1]:
        if i == min(m_list):
            m = m_list.index(i)
            break
    m_list[0], m_list[m] = m_list[m], m_list[0]
    answer = 0
    for i in m_list[::-1]:
        for j in range(len(m_list)):
            answer += i * 10**j
    return answer

T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int, input()))
    print(f'#{tc} {min_num(num_list)} {max_num(num_list)}')
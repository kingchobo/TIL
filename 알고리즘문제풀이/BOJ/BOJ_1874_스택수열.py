N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
sub_list = [i for i in range(1, N+1)]
my_stack = []
answer = []

while True:
    try:
        if len(arr) == 0:
            for i in answer:
                print(i)
            break
        if my_stack and my_stack[-1] == arr[0]:
            del my_stack[-1]
            del arr[0]
            answer.append('-')
        else:
            my_stack.append(sub_list.pop(0))
            answer.append('+')
    except:
        print('NO')
        break
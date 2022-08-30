import sys
n = int(sys.stdin.readline().strip())
# 재귀 함수로 피보나치수를 구할 시의 출력 회수도 피보나치 수열
# 따라서 dp를 이용하여 해당 실행 횟수를 구하면 된다.
# 그런데 문제에서 주어지는 숫자의 크기가 너무 커서 메모리 초과가 발생
# 원형 큐를 이용하여 메모리를 줄이자
# DP
def fibo(n):
    global cnt
    arr = [0, 1]
    for i in range(2, n+1):
        arr[i % 2] = arr[0] + arr[1]
        cnt += 1
    return arr[n % 2]

cnt = -1

print(fibo(n)%1000000007, cnt%1000000007)
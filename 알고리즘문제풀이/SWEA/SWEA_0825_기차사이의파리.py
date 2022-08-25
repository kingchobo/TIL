for tc in range(int(input())):
    d,a,b,f=map(int,input().split())
    print(f'#{tc+1} {f*(d/(a+b))}')
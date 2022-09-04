l = int(input())
string = input()
M = 1234567891
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z']
num_list = []
for i in string:
    num_list.append(alphabet.index(i) + 1)

ans = 0
for i in range(l):
    ans += num_list[i] * (31**i) % M
print(ans % M)
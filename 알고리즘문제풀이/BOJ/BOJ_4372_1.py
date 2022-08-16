def is_all_one(num):
    for i in str(num):
        if i != 1:
            return False
    return True

while True:
    try:
        n = int(input())
        i = 1
        while True:
            if is_all_one(n*i):
                print(len(str(n*i)))
                break
            else:
                i += 1
    except:
        break
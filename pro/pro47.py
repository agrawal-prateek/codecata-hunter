def rounding():
    n = int(input())
    k = int(input())
    bas = 10
    c = 0
    while (True):
        tn = bas * n
        t = tn
        while (t % 10 == 0):
            c += 1
            t //= 10
        if c == 4:
            print(tn)
            break
        c = 0
        bas += 10


try:
    rounding()
except:
    print('invalid')

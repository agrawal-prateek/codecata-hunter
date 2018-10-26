def insti():
    n = int(input())
    k = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    c = 0
    for i in l:
        if i != 5 and i >= k:
            c = c + 1
    print(c)


try:
    insti()
except:
    print('invalid')

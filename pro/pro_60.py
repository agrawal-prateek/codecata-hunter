def pro_60():
    n = int(input())
    c = 3
    co = 1
    i = 1
    r = c
    out = 0
    while (True):
        c -= 1
        i += 1
        if i >= n:
            co += 1
            out = 1
        if c == 1:
            c = 2 * r
            r = c
            i += 1
            if out == 1:
                break

    print(co)


pro_60()

try:
    s1, s2 = input().split()
    s1, s2 = list(s1), list(s2)

    i = 0
    while i < len(s1):
        if s1[i] in s2:
            s2.remove(s1[i])
            del s1[i]
        else:
            i += 1
    print(max(len(s1), len(s2)))
except Exception as e:
    print('Invalid Input')

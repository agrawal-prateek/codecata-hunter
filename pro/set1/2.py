def lowest(s, k, ans):
    if not k:
        ans.append(s)
    elif len(s) <= k:
        pass
    else:
        m = min(s[:k + 1])
        i = s[:k + 1].index(m)
        ans.append(m)
        lowest(s[i + 1:], k - i, ans)


try:
    s, k = [x for x in input().split()]
    k = int(k)
    ans = []
    lowest(s, k, ans)
    print(*ans, sep='')
except Exception as e:
    print('Invalid Input')

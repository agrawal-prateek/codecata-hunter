try:
    ans = set()
    come = set()
    n = int(input())
    arr = [int(x) for x in input().split()]
    for i in arr:
        if i in come:
            ans.add(i)
        else:
            come.add(i)
    if len(ans) == 0:
        print('unique')
    else:
        print(*ans)
except Exception as e:
    print('Invalid Input')

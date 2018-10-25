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
    print(*ans)
except Exception as e:
    print('Invalid Input')
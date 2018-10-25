try:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = set()
    for i in range(len(arr)):
        if arr[i] == i:
            ans.add(i)
    print(0) if not ans.__len__() else print(*ans)
except Exception as e:
    print('Invalid Input')

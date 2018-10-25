try:
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n == 1 and arr[0] == 0:
        print(0)
    else:
        arr = sorted(arr, reverse=True)
        if arr[0] == 0:
            del arr[0]
            arr.append(0)
        print(*arr, sep='')
except Exception as e:
    print('Invalid Input')

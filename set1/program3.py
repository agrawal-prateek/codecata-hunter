try:
    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = set()
    for i in range(len(arr)):
        ans.discard(arr[i]) if arr[i] in ans else ans.add(arr[i])
    print(ans.pop())
except Exception as e:
    print('Invalid Input')

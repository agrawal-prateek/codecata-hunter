n, g1, g2 = map(int, input().split())
if n % 2 == 0:
    n1 = n // 2
    if n1 % (g1 + g2) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

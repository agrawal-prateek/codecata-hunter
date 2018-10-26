try:
    s1, s2 = input().split()
    c = len(s1) + 1
    r = len(s2) + 1
    dp = [[0 for i in range(c)] for i in range(r)]
    for i in range(1, r):
        dp[i][0] = i
    dp[0] = [i for i in range(1, c)]
    for i in range(1, r):
        for j in range(1, c):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    print(dp[r - 1][c - 1])
except Exception as e:
    print('Invalid Input')
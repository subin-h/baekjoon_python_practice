N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    Ti, Pi = schedule[i]
    dp[i] = dp[i + 1]

    if i + Ti <= N:
        dp[i] = max(dp[i], Pi + dp[i + Ti])

print(dp[0])




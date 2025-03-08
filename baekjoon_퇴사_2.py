N = int(input())
dp =[0] * N
list_num = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    T_num, P_num = list_num[i]
    if T_num + i <= N:
        dp[i] = P_num

for j in range(N-2,-1,-1):
    data=list_num[j]
    if data[0] + j < N:
        dp[j] = max(dp[j+1],dp[j] + dp[data[0] + j])
    else:
        dp[j] = max(dp[j],dp[j+1])

print(max(dp))

N,M = map(int,input().split())
candy = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,M):
    candy[0][i] += candy[0][i-1]
for i in range(1,N):
    candy[i][0] += candy[i-1][0]

for i in range(1,N):
    for j in range(1,M):
        candy[i][j] += +max(candy[i][j-1],candy[i-1][j])
        
print(candy[-1][-1])
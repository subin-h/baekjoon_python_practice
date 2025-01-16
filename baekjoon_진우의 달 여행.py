N,M = map(int,input().split())
fuels = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(M):
        if j == 0 :
            fuels[i][j] = fuels[i][j] + min(fuels[i-1][j], fuels[i-1][j+1])
        elif j == M-1:
            fuels[i][j] = fuels[i][j] + min(fuels[i-1][j], fuels[i-1][j-1])
        else:
            fuels[i][j] = fuels[i][j] + min(fuels[i-1][j], fuels[i-1][j-1], fuels[i-1][j+1])
print(fuels)
print(min(fuels[N-1]))
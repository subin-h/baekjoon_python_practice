N,M = map(int,input().split())
min_change = float('inf')
board = [list(input().strip()) for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]
W = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i%2) == (j%2):
            if board[i][j] != 'B':
                B[i][j] = 1
            else:
                W[i][j] = 1
        else:
            if board[i][j] != 'W':
                B[i][j] = 1
            else:
                W[i][j] = 1

for i in range(N-8+1):
    for j in range(M-8+1):
        B_sum = sum(B[x][y] for x in range(i,i+8) for y in range(j,j+8))
        W_sum = sum(W[x][y] for x in range(i,i+8) for y in range(j,j+8))
        min_change = min(min_change,B_sum,W_sum)

print(min_change)
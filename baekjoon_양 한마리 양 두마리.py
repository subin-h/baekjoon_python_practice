import sys
sys.setrecursionlimit(10**6)

T=int(input())
def dfs(x,y):
    if x<= -1 or x >= H or y <= -1 or y>= W:
        return False
    if graph[x][y] == '#':
        graph[x][y] = '.'
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for i in range(T):
    H,W=map(int,input().split())
    graph=[list(input().strip()) for _ in range(H)]
    result =0
    for i in range(H):
        for j in range(W):
            if graph[i][j]=='#':
                dfs(i,j)
                result +=1
    print(result)
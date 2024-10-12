import sys
from collections import deque
N,M=map(int,input().split())
matrix=[list(sys.stdin.readline().strip()) for _ in range(1,N+1)]
def bfs(x,y):
    count=0
    queue=deque()
    queue.append([x,y])
    while queue:
        x,y=queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny=x+dx,y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny]=='X':
                continue
            else:
                if matrix[nx][ny]=='P':
                    count+=1
                matrix[nx][ny]='X'
                queue.append([nx,ny])
    return count

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='I':
            result=bfs(i,j)
if result == 0:
    print('TT')
else:
    print(result)
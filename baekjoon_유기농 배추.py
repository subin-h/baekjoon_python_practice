import sys
from collections import deque
T=int(input())
for _ in range(T):
   M,N,K=map(int,input().split())
   matrix=[[0]*M for _ in range(N)]
   for _ in range(K):
      y,x=map(int,sys.stdin.readline().split())
      matrix[x][y]=1
   def bsf(x1, y1):
      queue=deque()
      queue.append([x1,y1])
      while queue:
         x,y=queue.popleft()
         for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny]==1:
               matrix[nx][ny]=0
               queue.append([nx,ny])
      return 0
   result=0
   for i in range(N):
      for j in range(M):
        if matrix[i][j]==1:
            bsf(i,j)
            result+=1
   print(result)
from collections import deque
N,M=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

def bfs(graph,N,M):
    queue=deque()
    queue.append([0,0])
    while queue:
        print(queue)
        x,y=queue.popleft()
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append([nx,ny])
    return graph[N-1][M-1]

print(bfs(graph, N, M))
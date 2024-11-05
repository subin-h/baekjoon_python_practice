# 플로이드 워셜 알고리즘
# 다른 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
# 거쳐 가는 노드를 기준으로 알고리즘 수행

INF = int(1e9)
n=int(input())
m=int(input())
graph=[[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셔 알고리즘 수행
# D23(2에서 3까지의 도달 거리): D21+D13 (k=거쳐가는 노드)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 최단거리 저장
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range (1, n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
# 노드를 매번 선형 탐색. 시간 복잡도 O(V2)
# 노드의 개수가 10,000개 이상 시 사용 어려움

import sys
input=sys.stdin.readline
INF=int(1e9)
#n=노드의 개수, m=간선의 개수
n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
visited=[False] * (n+1) # 방문 표시
distance = [INF] * (n+1) # 최단 거리 테이블

for _ in range(m):
    a,b,c=map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

        #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    def get_smallest_node():
        min_value=INF
        index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
        for i in range(1,n+1):
            if distance[i] < min_value and not visited[i]:
                min_valuse = distance[i]
                index = i
        return index
    
    def dijkstra(start):
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        for i in range(n-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
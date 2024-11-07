# 위상 정렬
# = 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

# 진입차수 = 특정한 노드로 들어오는 간선의 개수
# 사이클이 발생하지 않은 경우를 명시

# 진입차수가 0인 노드를 큐에 스택

from collections import deque

v,e = map(int, input().split())
# 모든 노드의 진입차수를 표시
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft() # now = index
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i, end =' ')

topology_sort()
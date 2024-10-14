#count로 계산하는 방법
N=int(input())
link=int(input())
list_=[[] for _ in range(N+1)]
visited=[False]*(N+1)
#count=0
def dfs(graph, v, visited):
    #global count
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            #count+=1
for _ in range(link):
    i,j=map(int,input().split())
    list_[i].append(j)
    list_[j].append(i)

dfs(list_, 1, visited)
print(sum(visited)-1)
#print(count)
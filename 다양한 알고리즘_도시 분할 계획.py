# 2024/11/05

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int, input().split())
edges = []
result = 0
parent = [0] * (M+1)

for i in range(M+1) :
    parent[i] = i

for i in range(M):
    a, b ,c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for i in edges:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N+1)

for i in range(0, N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union(parent, b, c)
    else:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")
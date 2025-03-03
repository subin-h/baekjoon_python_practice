def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    total_cost = 0
    count = 0

    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):

            if count == n-1:
                break
            
            union_parent(parent, a, b)
            total_cost += cost
            count += 1
    
    return total_cost
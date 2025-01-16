N=int(input())
length = list(map(int,input().split()))
cost = list(map(int,input().split()))
pre_cost = cost[0]
total = 0
for i in range(N-1):
    if pre_cost <= cost[i]:
        total += (pre_cost*length[i])
    else:
        pre_cost = cost[i]
        total += (pre_cost*length[i])

print(total)
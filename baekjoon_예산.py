N = int(input())
budget = list(map(int,input().split()))
M = int(input())

if sum(budget) <= M:
    print(max(budget))
else:
    start = 0
    end = M
    while(start <= end):
        total_cost = 0
        mid = (start+end)//2
        for i in budget:
            if i <= mid:
                total_cost += i
            else:
                total_cost += mid
        if total_cost <= M:
            start = mid + 1
        else: 
            end = mid - 1
    print(end)


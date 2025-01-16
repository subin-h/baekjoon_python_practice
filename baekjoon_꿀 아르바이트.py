n,m = map(int,input().split())
money_ = list(map(int,input().split()))
current_sum = sum(money_[:m])
max_sum = current_sum

for i in range(m,n):
    current_sum = current_sum - money_[i-m] + money_[i]
    max_sum = max(max_sum,current_sum)

print(max_sum)

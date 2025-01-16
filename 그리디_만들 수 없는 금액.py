N = int(input())
money = sorted(list(map(int, input().split())))
storage = []

for i in range(N):
    make_money = 0
    for j in money[i:]:
        make_money += j
        storage.append(make_money)

money_list = sorted(set(storage))

for k in range(1, sum(money)):
    if k not in money_list :
        print(k)
        break
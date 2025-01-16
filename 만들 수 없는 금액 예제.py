N=int(input())
coins = sorted(list(map(int,input().split())))
# target = coins에 저장된 리스트의 원소로 표현할 수 있는지 확인하기 위해 설정
target = 1 # 표현해야 하는 가장 작은 값

# target은 표현할 수 있는 값에서 +1한 값 = 즉, 구할 수 없는 가장 작은 값
for coin in coins:
    if target < coin:
        print(target)
        break
    else:
        target += coin
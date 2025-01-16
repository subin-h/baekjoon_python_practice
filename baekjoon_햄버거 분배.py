N,K = map(int,input().split())
list_ = list(input().strip())
people, burgers = [],[]

people = [i for i in range(N) if list_[i] == 'P']
burgers = [i for i in range(N) if list_[i] == 'H']

answer = 0
i,j = 0,0

while i < len(people) and j < len(burgers):
    if abs(people[i] - burgers[j]) <= K:
        answer +=1
        i += 1
        j += 1
    elif people[i] < burgers[j]:
        i += 1
    else:
        j += 1

print(answer)


from collections import Counter,defaultdict

T = int(input())
for i in range(T):
    N = int(input())
    team = list(map(int,input().split()))
    count = Counter(team)
    score = [i for i in team if count[i] >= 6]

    team_sum = defaultdict(int)
    for idx, num in enumerate(score):
        team_sum[num] += idx
    
    print(team_sum)

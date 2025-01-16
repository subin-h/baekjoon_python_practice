import sys
T=int(input())
for i in range(T):
    N=int(input())
    rank = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    total=1
    rank.sort(key=lambda x: x[1])
    limit = rank[0][0]
    for single in rank:
        if single[0] < limit:
            limit = single[0]
            total += 1
    print(total)


    

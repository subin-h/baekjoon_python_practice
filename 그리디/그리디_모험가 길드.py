N=int(input())
ch_horror = sorted(list(map(int,input().split())))
group=0
group_size = []

for i in ch_horror :
    group_size.append(i)
    if max(group_size) - len(group_size) <= 0:
        group += 1
        group_size = []

print(group)
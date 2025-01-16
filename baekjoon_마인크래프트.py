N,M,B = map(int, input().split())
grand = [list(map(int,input().split())) for i in range(N)]
min_time = float('inf')
min_height = -1
for height in range(257):
    total = 0
    block = B
    for i in range(N):
        for j in range(M):
            if grand[i][j] < height:
                total += (height - grand[i][j])
                block -= height-grand[i][j]
            else:
                total += 2*(grand[i][j] - height)
                block += grand[i][j] - height
    if block < 0:
        continue
    
    if total < min_time:
        min_time = total
        min_height = height
    elif total == min_time:
        min_height = max(height,min_height)

print(min_time, min_height)
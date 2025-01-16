from collections import deque
T = int(input())
for _ in range(T):
    fin_list = []
    N,M = map(int,input().split())
    priority = deque(map(int,input().split()))

    queue = deque([(i, priority[i]) for i in range(N)])
    count = 0

    while queue:
        dx = queue.popleft()
        if any(data[1] > dx[1] for data in queue):
            queue.append(dx)
        else:
            count += 1
            if dx[0] == M:
                print(count)
                break
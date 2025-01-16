from collections import deque
N,K = map(int,input().split())
queue = deque([i for i in range(1,N+1)])
count = 0
result = []
while(queue):
    count += 1
    M=queue.popleft()
    if count == K:
        count = 0
        result.append(M)
    else:
        queue.append(M)

answer = ", ".join(map(str,result))
print(f"<{answer}>")
        

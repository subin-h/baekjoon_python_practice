from collections import deque
N,K=map(int,input().split())
arr=deque([i for i in range(1,N+1)])
while True:
    if len(arr)-K+1<K:
        break
    else:
        arr.rotate(-1)
        for _ in range(K-1):
            arr.popleft()

if len(arr)<=K:
    print(arr[0])
else:
    print(arr[K])

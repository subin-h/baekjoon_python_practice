from collections import deque
import sys
N=int(input())
que=deque()
for _ in range(N):
    K=sys.stdin.readline().split()
    if K[0]=='push':
        que.append(K[1])
    elif K[0]=='front':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
    elif K[0]=='back':
        if len(que)==0:
            print(-1)
        else:
            print(que[-1])
    elif K[0]=='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif K[0]=='size':
        print(len(que))
    elif K[0]=='pop':
        if len(que)==0:
            print(-1)
        else:
            print(que[0])
            que.popleft()
    